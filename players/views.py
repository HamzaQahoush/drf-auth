from django.shortcuts import render
from rest_framework import generics, serializers  # add
from .models import Players
from .serializers import PlayersSerializers
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PlayersListView(generics.ListCreateAPIView):
    serializer_class = PlayersSerializers
    queryset = Players.objects.all()


class PlayersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayersSerializers
    queryset = Players.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
