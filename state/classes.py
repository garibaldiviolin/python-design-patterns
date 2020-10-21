from abc import ABC, abstractmethod


class InvalidSwitchException(Exception):
    """Indicates that there is no next status."""
    pass


class OrderState(ABC):
    state_slug = None  # must be declared

    def __init__(self, order):
        self._order = order

    @abstractmethod
    def perform_action(self):  # pragma: no cover
        """This method performs the actions of this state and also
        switches to the next state. If there is no next state, it should
        raise a InvalidSwitchException.
        """
        pass


class TerminativeOrderState(OrderState):
    def perform_action(self):
        raise InvalidSwitchException(
            f"A {self.state_slug} order cannot switch to another state."
        )


class DeliveredOrderState(TerminativeOrderState):
    state_slug = "delivered"


class TransitionalOrderState(OrderState):
    next_state_class = None  # Must be set with the next state class

    def switch_state(self):
        next_state = self.next_state_class(self._order)
        self._order.switch_state(next_state)
        print(f"Order state was switched to {next_state.state_slug}.")

    def perform_action(self):
        self.switch_state()


class ShippedOrderState(TransitionalOrderState):
    state_slug = "shipped"
    next_state_class = DeliveredOrderState


class CreatedOrderState(TransitionalOrderState):
    state_slug = "created"
    next_state_class = ShippedOrderState


class Order:
    def __init__(self):
        self._state = CreatedOrderState(self)

    def show_state(self):
        print(f"The order is currently {self._state.state_slug}.")

    def switch_state(self, new_state):
        self._state = new_state

    def proceed(self):
        self._state.perform_action()
