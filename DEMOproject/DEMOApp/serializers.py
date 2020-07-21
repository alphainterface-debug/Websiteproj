from rest_framework import serializers
from . models import Contact,customerscore,surveyscore

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model= Contact
        fields = '__all__'

class CustSerializer(serializers.ModelSerializer):

    class Meta:
        model= customerscore
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model= surveyscore
        fields = '__all__'