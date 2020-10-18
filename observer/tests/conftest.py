from ..classes import (
    EmailAddress,
    WhatsAppAddress,
    Alert
)

import pytest


@pytest.fixture
def email_address():
    return EmailAddress("python@email.com")


@pytest.fixture
def whatsapp_address():
    return WhatsAppAddress("+99 111 5555-5555")


@pytest.fixture
def alert():
    return Alert()


@pytest.fixture
def alert_with_addresses(alert, email_address, whatsapp_address):
    alert.add_address(email_address)
    alert.add_address(whatsapp_address)
    return alert
