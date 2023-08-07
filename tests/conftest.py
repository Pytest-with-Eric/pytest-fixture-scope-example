"""Conftest file to define fixtures at different scopes."""
import pytest
import smtplib


@pytest.fixture(scope='function', autouse=True)
def smtp_connection():
    print("SMTP Connection fixture start")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("SMTP Connection Tear Down")