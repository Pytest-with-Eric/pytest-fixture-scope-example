def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    print("Test EHLO in Function...")
    assert response == 250
    assert b"smtp.gmail.com" in msg


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    print("Test NOOP in Function...")
    assert response == 250
    assert b"OK" in msg

# class TestSMTP:
#     def test_ehlo(self):
        # response, msg = smtp_connection.ehlo()
        # print("Test EHLO in Class...")
        # assert response == 250
        # assert b"smtp.gmail.com" in msg

#     def test_noop(self):
#         response, msg = smtp_connection.noop()
#         print("Test NOOP in Class...")
#         assert response == 250
#         assert b"OK" in msg


# To Test various scopes and heirarchy, use different fixtures with auto use