from django.views import generic

from .models import Moof


class MoofDetailView(generic.ListView):
    model = Moof
