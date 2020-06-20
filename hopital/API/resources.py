from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from hopital.API.pesmissions import OnlyDoctor
from hopital.API.serializers import PatientSerializer, PatientGetSerializer, DoctorSerializer, SpecializationSerializer, \
    DoctorGetSerializer
from hopital.models import Patient, Doctor, Specialization


class PatientViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return PatientGetSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.request.method.lower() == 'post':
            return []
        return super().get_permissions()


class DoctorViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return DoctorGetSerializer
        return super().get_serializer_class()


class SpecializationViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()
    permission_classes = [OnlyDoctor, ]
