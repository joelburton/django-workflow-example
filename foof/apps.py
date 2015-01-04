from django.apps import AppConfig
import watson


class FoofAppConfig(AppConfig):
    name = 'foof'

    def ready(self):
        watson.register(self.get_model("Moof"), store=('published',))
