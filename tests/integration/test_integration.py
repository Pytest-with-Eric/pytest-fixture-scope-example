# my_project/tests/integration/test_integration.py

from math_operations.operations import add_numbers


def test_add_numbers_integration(package_scope_fixture, session_scope_fixture):
    assert add_numbers(5, 5) == 10
