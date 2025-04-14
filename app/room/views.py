from viewflow.urls import ModelViewset
from . import models

class CityViewset(ModelViewset):
    model = models.Room