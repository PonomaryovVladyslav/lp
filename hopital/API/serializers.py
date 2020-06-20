from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.utils.serializer_helpers import ReturnDict

from hopital.models import Patient, Doctor, Specialization


class PatientSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(required=True)

    class Meta:
        model = Patient
        fields = ['username', 'first_name', 'last_name', 'password', 'sex', 'ssn', 'birthday',
                  'mobile_number']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class PatientGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['username', 'first_name', 'last_name', 'sex', 'ssn', 'birthday',
                  'mobile_number']


class DoctorSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(required=True)
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'password', 'sex', 'birthday', 'specializations', 'id']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['title', 'id']


class DoctorGetSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    specializations = SpecializationSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'sex', 'birthday', 'specializations', 'id']
