from unittest.mock import patch

import pytest

from ..classes import (
    ElectronicAddress,
    EmailAddress,
    WhatsAppAddress,
)


def test_create_electronic_address_instance():
    with pytest.raises(TypeError) as exc:
        ElectronicAddress()

    assert str(exc.value) == (
        "Can't instantiate abstract class ElectronicAddress with "
        "abstract methods send_alert"
    )


def test_email_address_class():
    assert issubclass(EmailAddress, ElectronicAddress) is True


def test_email_address_instance(email_address):
    assert email_address._address == "python@email.com"


@patch("builtins.print")
def test_email_address_send_email(print_mock, email_address):
    message = "This is a message."
    email_message = "Message 'This is a message.' sent to python@email.com"

    email_address.send_email(message)

    print_mock.assert_called_once_with(email_message)


@patch("observer.classes.EmailAddress.send_email")
def test_email_address_send_alert(send_email_mock, email_address):
    message = "What a message!"

    email_address.send_alert(message)

    send_email_mock.assert_called_once_with(message)


def test_whatsapp_address_class():
    assert issubclass(WhatsAppAddress, ElectronicAddress) is True


def test_whatsapp_address_instance(whatsapp_address):
    assert whatsapp_address._phone_number == "+99 111 5555-5555"


@patch("builtins.print")
def test_whatsapp_address_send_email(print_mock, whatsapp_address):
    message = "Something is wrong."
    email_message = "Message 'Something is wrong.' sent to +99 111 5555-5555"

    whatsapp_address.send_email(message)

    print_mock.assert_called_once_with(email_message)


@patch("observer.classes.WhatsAppAddress.send_email")
def test_whatsapp_address_send_alert(send_message_mock, whatsapp_address):
    message = "Top secret!"

    whatsapp_address.send_alert(message)

    send_message_mock.assert_called_once_with(message)


def test_alert_addresses(alert):
    assert alert._addresses == []


def test_alert_add_email_address(alert, email_address):
    alert.add_address(email_address)

    assert alert._addresses == [email_address]


def test_alert_add_whatsapp_address(alert, whatsapp_address):
    alert.add_address(whatsapp_address)

    assert alert._addresses == [whatsapp_address]


def test_alert_remove_address(alert_with_addresses, email_address,
                              whatsapp_address):
    alert_with_addresses.remove_address(email_address)

    assert alert_with_addresses._addresses == [whatsapp_address]


@patch("observer.classes.WhatsAppAddress.send_alert")
@patch("observer.classes.EmailAddress.send_alert")
def test_trigger_alert(email_alert_mock, whatsapp_alert_mock,
                       alert_with_addresses):
    alert_message = "System was invaded!"
    alert_with_addresses.trigger_alert()

    email_alert_mock.assert_called_once_with(alert_message)
    whatsapp_alert_mock.assert_called_once_with(alert_message)
