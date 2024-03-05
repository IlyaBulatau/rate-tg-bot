import json


class BrokerSerializer:

    def __init__(self, data: bytes):
        self.data = data

    def serialize(self) -> list[dict] | dict:
        result = json.loads(self.data.decode().replace("'", '"'))
        return result