"""Conftest file to define fixtures at different scopes."""
import pytest
import smtplib
from contextlib import contextmanager


# @pytest.fixture(scope="module", autouse=True)
# def smtp_connection() -> smtplib.SMTP:
#     """
#     A fixture to create an SMTP connection.

#     Returns:
#         An SMTP connection
#     """
#     print("SMTP Connection fixture start")
#     yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
#     print("SMTP Connection Tear Down")


# Demonstrate how to share a base fixture with different scopes
@contextmanager
def smtp_connection_base() -> smtplib.SMTP:
    """
    A fixture to create an SMTP connection.

    Returns:
        An SMTP connection
    """
    print("SMTP Connection fixture start")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("SMTP Connection Tear Down")


# Fixture with module scope
@pytest.fixture(scope="module")
def smtp_connection():
    with smtp_connection_base() as result:
        yield result
