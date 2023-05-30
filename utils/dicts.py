def get_val(collection, key, default='git'):
    """Функция, возвращающая элемент в словаре"""

    if collection.get(key):
        return collection.get(key)
    else:
        return default


