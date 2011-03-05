import gc

snapshot_objects = set()

def snapshot():
    snapshot_objects.clear()
    gc.collect()
    snapshot_objects.update(id(o) for o in gc.get_objects())

def get_new_objects():
    gc.collect()
    for o in gc.get_objects():
        if id(o) not in snapshot_objects:
            yield o

def group_by_class():
    result = {}
    for o in get_new_objects():
        try:
            cls = o.__class__
        except AttributeError:
            cls = o

        key = cls.__module__ + '.' + cls.__name__
        try:
            result[key].append(o)
        except KeyError:
            result[key] = [o]

    return result