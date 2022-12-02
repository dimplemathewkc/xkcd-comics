from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

urlpatterns = [
    path("comics/", views.ComicView.as_view(), name="comics"),
    path("^", include(router.urls)),
]
