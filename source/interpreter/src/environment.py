class Environment():
    def __init__(self, parent_env):
        self._parent_env = parent_env
        self._env = dict()

    def get(self, key):
        value = self._env.get(key, None)
        if not value:
            value = self._parent_env.get(key)
        return value

    def set(self, key, value):
        self._env[key] = value
