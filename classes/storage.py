from exeptions import NotFoundItems, NotEnoughItems, NotPlaceForItems
from classes.base_storage import BaseStorage


class Storage(BaseStorage):
    def __init__(self):
        self._items = dict()
        self._capacity = 0

    @property
    def capacity(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    def add(self, title, count):
        if count > self.get_free_space():
            raise NotPlaceForItems('Нет свободного места')
        self.items[title] = self.items.get(title, 0) + count

    def remove(self, title, count):
        if self.items.get(title) is None:
            raise NotFoundItems('Нет такого товара')
        if count < self.items.get(title):
            self.items[title] = self.items.get(title) - count
        elif count > self.items[title] or self.items[title] == 0:
            raise NotEnoughItems('Не хватает товаров')

    def get_unique_items_count(self):
        return len(set(self.items.keys()))

    def get_items(self):
        return self.items

    def get_free_space(self):
        return self.capacity - sum(self.items.values())
