DEFAULTS = {
    "STORAGE": {
        "type": "local",
        "path": "./storage",
    }
    "TITLE_PROPERTY": "title",
    "LINK_PROPERTY": "link",
    "MHTML_PROPERTY": "mhtml",
}


class Setting:
    def __init__(self, user_settings=None, defaults=None) -> None:
        self.user_settings = user_settings or {}
        self.defaults = defaults or {}

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid pagehub setting: '%s'" % attr)
        try:
            val = self.user_settings[attr]
        except KeyError:
            val = self.defaults[attr]
        setattr(self, attr, val)
        return val


pagehub_settings = Setting(user_settings={}, defaults=DEFAULTS)  # TODO
