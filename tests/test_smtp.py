def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    print("Test EHLO 1 ")
    assert response == 250
    assert b"smtp.gmail.com" in msg


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    print("Test NOOP 1 ")
    assert response == 250
    assert b"OK" in msg

class TestSMTP1:
    def test_ehlo(self, smtp_connection):
        response, msg = smtp_connection.ehlo()
        print("Test EHLO 1 in Class...")
        assert response == 250
        assert b"smtp.gmail.com" in msg

    def test_noop(self, smtp_connection):
        response, msg = smtp_connection.noop()
        print("Test NOOP 1 in Class...")
        assert response == 250
        assert b"OK" in msg