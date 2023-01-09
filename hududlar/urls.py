from django.urls import path

from hududlar.views import CreateHudud, CreateVaqt, HududlarView, HududlarVaqt, AutoCreateHudud

urlpatterns = [
    path("hudud/create/", CreateHudud.as_view()),
    path("hududlar/", HududlarView.as_view()),
    path("hudud/", HududlarVaqt.as_view()),

    path("hudud/autocreate/", AutoCreateHudud.as_view()),
    path("vaqt/create/", CreateVaqt.as_view()),
]