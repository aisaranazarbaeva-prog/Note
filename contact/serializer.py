from rest_framework import serializers
from .models import Contacts

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = (
            'name',
            'phone_number',
            'created_at',


        )
        read_only_fields =(
            'name',
            'phone_number'
            'created_at',

        )