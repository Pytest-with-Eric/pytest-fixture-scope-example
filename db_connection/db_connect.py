class MockDB:
    def __init__(self):
        self.connection = "Connected"

    def disconnect(self):
        self.connection = "Disconnected"
