from dataclasses import fields
from rest_framework import serializers
from .models import Synth


class SynthSerializer(serializers.HyperlinkedModelSerializer):
    synth_url = serializers.ModelSerializer.serializer_url_field(
        view_name='synth_detail')

    class Meta:
        model = Synth
        fields = ('id', 'name', 'synth_type', 'filter_amount',
                  'delay_amount', 'synth_url')
