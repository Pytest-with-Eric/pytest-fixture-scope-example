from math_operations.operations import add_numbers, subtract_numbers
import pytest


@pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="session")
# @pytest.fixture(scope="package")
# @pytest.fixture(scope="module")
def my_fixture():
    print("\nSetup my_fixture")
    yield
    print("Teardown my_fixture")


# function scope


def test_add_numbers(my_fixture):
    assert add_numbers(1, 2) == 3


def test_subtract_numbers(my_fixture):
    assert subtract_numbers(2, 1) == 1


# class scope


class TestClass:
    def test_add_numbers_class(self, my_fixture):
        assert add_numbers(3, 2) == 5

    def test_subtract_numbers_class(self, my_fixture):
        assert subtract_numbers(3, 2) == 1


## using confest.py
def test_add_numbers(function_scope_fixture):
    assert add_numbers(1, 2) == 3


def test_subtract_numbers(function_scope_fixture):
    assert subtract_numbers(2, 1) == 1


class TestClass:
    def test_add_numbers_class(self, class_scope_fixture):
        assert add_numbers(3, 2) == 5

    def test_subtract_numbers_class(self, class_scope_fixture):
        assert subtract_numbers(3, 2) == 1


# def test_add_numbers(function_scope_fixture, module_scope_fixture, session_scope_fixture):
#     assert add_numbers(1, 2) == 3

# def test_subtract_numbers(function_scope_fixture, module_scope_fixture, session_scope_fixture):
#     assert subtract_numbers(2, 1) == 1

# class TestClass:
#     def test_add_numbers_class(self, class_scope_fixture, package_scope_fixture, session_scope_fixture):
#         assert add_numbers(3, 2) == 5

#     def test_subtract_numbers_class(self, class_scope_fixture, package_scope_fixture, session_scope_fixture):
#         assert subtract_numbers(3, 2) == 1
