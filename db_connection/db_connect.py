import random

class MockDB:
    def __init__(self):
        self.id = random.randint(1, 1000)
        self.connection = "Connected"

    def disconnect(self):
        self.connection = "Disconnected"
