from django.apps import AppConfig
import watson


class FoofAppConfig(AppConfig):
    name = 'foof'

    def ready(self):
        # Store Moof objects in searchtable; add published to the meta-information watson stores
        watson.register(self.get_model("Moof"), store=('published',))
