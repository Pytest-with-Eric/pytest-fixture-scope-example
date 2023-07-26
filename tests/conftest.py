# conftest.py

import pytest


@pytest.fixture(scope="function")
def function_scope_fixture():
    print("\nSetting up function-scope fixture")
    yield
    print("Tearing down function-scope fixture")


@pytest.fixture(scope="class")
def class_scope_fixture():
    print("\nSetting up class-scope fixture")
    yield
    print("Tearing down class-scope fixture")


@pytest.fixture(scope="module")
def module_scope_fixture():
    print("\nSetting up module-scope fixture")
    yield
    print("Tearing down module-scope fixture")


@pytest.fixture(scope="package")
def package_scope_fixture():
    print("\nSetting up package-scope fixture")
    yield
    print("Tearing down package-scope fixture")


@pytest.fixture(scope="session")
def session_scope_fixture():
    print("\nSetting up session-scope fixture")
    yield
    print("Tearing down session-scope fixture")
