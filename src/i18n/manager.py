from .es import Strings as EsStrings
from .en import Strings as EnStrings
from config.settings import Settings

class I18n:
    def __init__(self):
        self._language = Settings.DEFAULT_LANGUAGE
        self._set_strings()

    def _set_strings(self):
        if self._language == "es":
            self.strings = EsStrings()
        else:
            self.strings = EnStrings()

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
        self._set_strings()

    def __getattr__(self, name):
        return getattr(self.strings, name)

# Sugerencia de tipo para habilitar el autocompletado en el IDE (usando español como esquema base)
i18n: EsStrings = I18n()
