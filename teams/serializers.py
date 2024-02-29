from .models import AboutPage, Contact, Groups, PersonalInfo
from rest_framework import serializers


class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
