import functools
import pickle


def save(fn):
    @functools.wraps(fn)
    def save_pickle(*args, **kwargs):
        try:
            with open('test_hashmap.pickle', 'rb') as f:
                loaded = pickle.load(f)
            return fn(loaded, *args, **kwargs)
        except FileNotFoundError:
            print('file not found')
        finally:
            with open('test_hashmap.pickle', 'wb') as f:
                pickle.dump(loaded, f)

    return save_pickle
