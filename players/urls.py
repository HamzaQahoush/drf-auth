from django.contrib import admin
from django.urls import path, include
from .views import PlayersListView, PlayersDetailView

urlpatterns = [
    path("", PlayersListView.as_view(), name="player_api"),
    path("<int:pk>", PlayersDetailView.as_view(), name="player_detail_api"),
]
