# def test_ehlo(smtp_connection):
#     response, msg = smtp_connection.ehlo()
#     assert response == 250
#     assert b"smtp.gmail.com" in msg


# def test_noop(smtp_connection):
#     response, msg = smtp_connection.noop()
#     assert response == 250
#     assert b"OK" in msg

class TestSMTP:
    def test_ehlo(self, smtp_connection):
        response, msg = smtp_connection.ehlo()
        print("\nTesting ehlo...")
        assert response == 250
        assert b"smtp.gmail.com" in msg

    def test_noop(self, smtp_connection):
        response, msg = smtp_connection.noop()
        print("\nTesting noop...")
        assert response == 250
        assert b"OK" in msg