from rest_framework import generics
from django.shortcuts import render

from .serializers import SynthSerializer
from .models import Synth

# Create your views here.


class SynthList(generics.ListCreateAPIView):
    queryset = Synth.objects.all()
    serializer_class = SynthSerializer


class SynthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Synth.objects.all()
    serializer_class = SynthSerializer
