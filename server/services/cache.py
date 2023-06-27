import redis
from typing import Any

class Cache:
    """Thin wrapper for the Redis cache.
    """
    def __init__(self, host = "redis", port = 6379):
        """Cache constructor.

        Args:
            host (str, optional): The Redis host. Defaults to "redis".
            port (int, optional): The Redis port. Defaults to 6379.
        """
        self.cache = redis.Redis(host = host, port = port)

    def get(self, key: str) -> bytes | None:
        """Get an object from the Redis cache.

        Args:
            key (str): The object key.

        Returns:
            bytes: An object from the Redis cache.
        """
        return self.cache.get(key)

    def set(self, key: str, value: Any, ex: int = None) -> bool | None:
        """Set an object in the Redis cache.

        Args:
            key (str): The object key.
            value (Any): The object.
            ex (int, optional): The cache expiration time. Defaults to None.

        Returns:
            bool: The status for whether an object was added to Redis.
        """
        return self.cache.set(key, value, ex)
        