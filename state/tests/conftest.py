from unittest.mock import Mock

from ..classes import (
    OrderState,
    TerminativeOrderState,
    DeliveredOrderState,
    TransitionalOrderState,
    Order,
)

import pytest


@pytest.fixture
def order():
    return Order()


@pytest.fixture
def order_mock():
    order = Mock()
    return order


@pytest.fixture
def order_state(order):
    class TestOrderState(OrderState):
        def perform_action(self):  # pragma: no cover
            pass

    return TestOrderState(order)


@pytest.fixture
def order_state_mock():
    order_state = Mock()
    order_state.perform_action = Mock()
    return order_state


@pytest.fixture
def delivered_order_state(order):
    return DeliveredOrderState(order)


@pytest.fixture
def terminative_order_state(order):
    terminative_order_state = TerminativeOrderState(order)
    terminative_order_state.state_slug = "finished"
    return terminative_order_state


@pytest.fixture
def transitional_order_state(order_mock):
    order_state = TransitionalOrderState(order_mock)
    return order_state
