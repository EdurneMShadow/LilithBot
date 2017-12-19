from telegram.ext import BaseFilter

class FilterDictadura(BaseFilter):
    def filter(self, message):
        return 'activar alzamiento del gran lider' in message.text
