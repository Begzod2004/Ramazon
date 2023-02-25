from django.urls import path

from hududlar.views import *

urlpatterns = [
    path('categoryvideo/', VideoCategoryList.as_view(), name='VideoCategory-list'),
    path('video/', VideoList.as_view(), name='video-list'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path("hudud/create/", CreateHudud.as_view()),
    path("hududlar/", HududlarView.as_view()),
    path("hudud/", HududlarVaqt.as_view()),
    path("hudud_id/<int:pk>", HududRetrieveAPIView.as_view()),
    path("vaqt_id/<int:pk>", VaqtRetrieveAPIView.as_view()),
    path("HududList/>", HududList.as_view()),
    path("hudud/autocreate/", AutoCreateHudud.as_view()),
    path("vaqt/create/", CreateVaqt.as_view()),
    path("VaqtList/>", VaqtList.as_view()),
#   Viloyat auto creator
    path("viloyat/autocreate/", AutoCreateViloyat.as_view()),

    path("viloyat/create/", CreateViloyat.as_view()),
    path("viloyatlar/", ViloyatView.as_view()),
    # path("viloyat/", VlarVaqt.as_view()),
    path("viloyat_id/<int:pk>", ViloyatRetrieveAPIView.as_view()),
    path("namoz_vaqti_id/<int:pk>", NamozVaqtiRetrieveAPIView.as_view()),
    path("ViloyatList/>", ViloyatList.as_view()),
    path("namoz_vaqt/create/", CreateNamozVaqti.as_view()),
    path("NamozvaqtList/>", NamozVaqtiList.as_view()),
  
 
]