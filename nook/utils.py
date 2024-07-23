import functools
import pickle


class HashMap:
    def __init__(self):
        self.array = [None for _ in range(100)]

    @staticmethod
    def __hash(key):
        count = 0
        for i in key:
            count += ord(i)
        return count

    def set(self, key, value):
        hashed = self.__hash(key) % len(self.array)
        if self.array[hashed] is None:
            self.array[hashed] = [(key, value)]
        else:

            for index, (k, v) in enumerate(self.array[hashed]):
                if k == key:
                    self.array[hashed][index] = (key, value)
                    return
            self.array[hashed].append((key, value))

    def get(self, key):
        hashed = self.__hash(key) % len(self.array)
        if self.array[hashed] is not None:
            for k, v in self.array[hashed]:
                if k == key:
                    return v
        return None

    def remove_item(self, key):
        hashed = self.__hash(key) % len(self.array)
        if self.array[hashed] is not None:
            if len(self.array[hashed]) == 1:
                self.array[hashed] = None
            else:
                for index, (k, v) in enumerate(self.array[hashed]):
                    if k == key:
                        self.array[hashed].pop(index)
                        return

    def __repr__(self):
        return f'{type(self)}'


def save(fn):
    @functools.wraps(fn)
    def save_pickle(*args, **kwargs):
        try:
            with open('hashmap.pickle', 'rb') as f:
                loaded = pickle.load(f)
            return fn(loaded, *args, **kwargs)
        except FileNotFoundError:
            print('file not found')
        finally:
            with open('hashmap.pickle', 'wb') as f:
                pickle.dump(loaded, f)

    return save_pickle