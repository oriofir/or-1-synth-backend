from django.urls import path, include
from . import views

urlpatterns = [
    # GET localhost:8000/synths
    # POST localhost:8000/Synths
    path('synths/', views.SynthList.as_view(), name='synth_list'),
    # PUT localhost:8000/synths/:id
    # DELETE localhost:8000/synths/:id
    path('synths/<int:pk>',
         views.SynthDetail.as_view(), name='synth_detail'),


]
