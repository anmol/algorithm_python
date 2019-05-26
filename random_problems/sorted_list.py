class SimpleList(object):
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)

class SortedList(SimpleList):
    def __init__(self, items=()):
        super(SortedList, self).__init__(items)
        self.sort()

    def add(self, item):
        super(SortedList, self).add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))

class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:self._validate(x)
        super(IntList, self).__init__(items)

    def add(self, item):
        self._validate(item)
        super(IntList, self).add(item)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only support integer values')

    def __repr__(self):
        return "IntList({!r})".format(list(self))


class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


