def test_db_function_1(db_function):
    print(f"Test with function-scope fixture, id: {db_function.id}")
    assert db_function.connection == "Connected"

def test_db_function_2(db_function):
    print(f"Test with function-scope fixture, id: {db_function.id}")
    assert db_function.connection == "Connected"

def test_db_module_1(db_module):
    print(f"Test with module-scope fixture, id: {db_module.id}")
    assert db_module.connection == "Connected"

def test_db_module_2(db_module):
    print(f"Test with module-scope fixture, id: {db_module.id}")
    assert db_module.connection == "Connected"

class TestDBClass:
    def test_db_class_1(self, db_class):
        print(f"Test with class-scope fixture, id: {db_class.id}")
        assert db_class.connection == "Connected"

    def test_db_class_2(self, db_class):
        print(f"Test with class-scope fixture, id: {db_class.id}")
        assert db_class.connection == "Connected"

def test_db_session_1(db_session):
    print(f"Test with session-scope fixture, id: {db_session.id}")
    assert db_session.connection == "Connected"

def test_db_session_2(db_session):
    print(f"Test with session-scope fixture, id: {db_session.id}")
    assert db_session.connection == "Connected"
