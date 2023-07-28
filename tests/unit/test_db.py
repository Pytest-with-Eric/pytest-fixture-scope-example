def test_db_function(db_function):
    assert db_function.connection == "Connected"

def test_db_module(db_module):
    assert db_module.connection == "Connected"

class TestDBClass:
    def test_db_class(self, db_class):
        assert db_class.connection == "Connected"

def test_db_session(db_session):
    assert db_session.connection == "Connected"
