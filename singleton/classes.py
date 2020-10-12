import inspect


class Configuration:
    _instance = None

    def __new__(self, *args, **kwargs):
        if inspect.stack()[1][3] != "get_instance":
            raise AttributeError(
                "You cannot instantiate Configuration class. "
                "Please use get_instance method."
            )
        return super().__new__(self, *args, **kwargs)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
