from abc import ABC, abstractmethod


class ElectronicAddress(ABC):
    """The subclasses of this one (Observer) is responsible for sending
    alert message with the specified format of the API (email, whatsapp,
    etc.).
    """
    @abstractmethod
    def send_alert(self, message):  # pragma: no cover
        pass


class EmailAddress(ElectronicAddress):
    def __init__(self, address):
        self._address = address

    def send_email(self, message):
        print(f"Message '{message}' sent to {self._address}")

    def send_alert(self, message):
        self.send_email(message)


class WhatsAppAddress(ElectronicAddress):
    def __init__(self, phone_number):
        self._phone_number = phone_number

    def send_email(self, message):
        print(f"Message '{message}' sent to {self._phone_number}")

    def send_alert(self, message):
        self.send_email(message)


class Alert:
    def __init__(self):
        self._addresses = list()

    def add_address(self, address):
        self._addresses.append(address)

    def remove_address(self, address):
        self._addresses.remove(address)

    def trigger_alert(self):
        for address in self._addresses:
            address.send_alert("System was invaded!")
