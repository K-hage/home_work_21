from classes.base_storage import BaseStorage


class Store(BaseStorage):
    def __init__(self):
        super().__init__()
        self._capacity = 100
