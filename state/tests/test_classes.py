from unittest.mock import Mock, MagicMock, patch

import pytest

from ..classes import (
    InvalidSwitchException,
    OrderState,
    TerminativeOrderState,
    DeliveredOrderState,
    TransitionalOrderState,
    ShippedOrderState,
    CreatedOrderState,
)


def test_invalid_switch_exception():
    assert issubclass(InvalidSwitchException, Exception) is True


def test_create_order_state_instance():
    with pytest.raises(TypeError) as exc:
        OrderState()

    assert str(exc.value) == (
        "Can't instantiate abstract class OrderState with abstract methods "
        "perform_action"
    )


def test_order_state(order_state, order):
    assert order_state.state_slug is None
    assert order_state._order == order


def test_terminative_order_state_class():
    assert issubclass(TerminativeOrderState, OrderState) is True


def test_terminative_order_state(terminative_order_state, order):
    order_state = TerminativeOrderState(order)
    order_state.state_slug = "finished"
    with pytest.raises(InvalidSwitchException) as exc:
        order_state.perform_action()

    str(exc.value) == "A finished order cannot switch to another state."


def test_delivered_order_state_class():
    assert issubclass(DeliveredOrderState, TerminativeOrderState) is True


def test_delivered_order_state(delivered_order_state):
    assert delivered_order_state.state_slug == "delivered"


def test_transitional_order_state_class():
    assert issubclass(TransitionalOrderState, OrderState) is True
    assert TransitionalOrderState.next_state_class is None


@patch("builtins.print")
def test_transitional_order_state_switch_state(print_mock,
                                               transitional_order_state,
                                               order_mock):
    next_state_mock = Mock(state_slug="this")
    transitional_order_state.next_state_class = MagicMock(
        return_value=next_state_mock
    )

    transitional_order_state.switch_state()

    transitional_order_state.next_state_class.assert_called_once_with(
        transitional_order_state._order
    )
    order_mock.switch_state.assert_called_once_with(next_state_mock)
    print_mock.assert_called_once_with(
        "Order state was switched to this."
    )


def test_transitional_order_state_perform_action(transitional_order_state):
    transitional_order_state.switch_state = Mock()

    transitional_order_state.perform_action()

    transitional_order_state.switch_state.assert_called_once_with()


def test_shipped_order_state_class():
    assert issubclass(ShippedOrderState, TransitionalOrderState)


def test_shipped_order_state(order):
    shipped_order_state = ShippedOrderState(order)
    assert shipped_order_state.state_slug == "shipped"
    assert shipped_order_state.next_state_class == DeliveredOrderState


def test_created_order_state_class():
    assert issubclass(CreatedOrderState, TransitionalOrderState)


def test_created_order_state(order):
    created_order_state = CreatedOrderState(order)
    assert created_order_state.state_slug == "created"
    assert created_order_state.next_state_class == ShippedOrderState


def test_order(order):
    assert isinstance(order._state, CreatedOrderState) is True


@patch("builtins.print")
def test_order_show_state(print_mock, order):
    order._state = DeliveredOrderState(order)
    order.show_state()

    print_mock.assert_called_once_with(
        "The order is currently delivered."
    )


def test_order_switch_state(order):
    new_state = ShippedOrderState(order)

    order.switch_state(new_state)

    assert order._state == new_state


def test_order_proceed(order, order_state_mock):
    order._state = order_state_mock

    order.proceed()

    order_state_mock.perform_action.assert_called_once_with()
