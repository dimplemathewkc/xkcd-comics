from django.core.cache import cache


def get_comics_from_cache(key):
    """
    Get all comics from cache.
    """
    return cache.get(key)


def set_comics_to_cache(key, value):
    """
    Set all comics to cache.
    """
    cache.set(key, value)


def delete_comics_from_cache(key):
    """
    Delete all comics from cache.
    """
    cache.delete(key)


def update_comics_in_cache(key, value):
    """
    Update all comics in cache.
    """
    cache.set(key, value)
