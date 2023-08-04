"""Conftest file to define fixtures at different scopes."""
import pytest
import smtplib

@pytest.fixture(scope='module')
def smtp_connection():
    print("\nCreating smtp connection")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("\nClosing smtp connection")