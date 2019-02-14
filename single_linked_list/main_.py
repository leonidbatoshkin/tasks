class List:
    """This class contains some "list's" class functionality"""

    def __init__(self, value=None, next_=None):
        self.value = value
        self.next_ = next_
        self._cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor + 1 >= len(str(self).replace(' ', '')):
            raise StopIteration()
        self._cursor += 1
        return int(str(self).replace(' ', '')[self._cursor])

    def __str__(self):
        if self.next_ is not None:
            return f'{self.value} {self.next_}'
        else:
            return f'{self.value}'

    def print(self):
        print(self)

    def append(self, value_to_add):
        self.next_ = List(self.next_, next_=value_to_add)
        return str(self)

    def __iadd__(self, other):
        for el in other:
            self.next_ = List(self.next_, next_=el)
        return self

    def print_reversed(self):
        #print(str(self)[::-1]) uncomment to output
        return str(self)[::-1]

    def __setattr__(self, key, val):
        self.__dict__[key] = val
        if key == '_value':
            self.value = val
            return self
