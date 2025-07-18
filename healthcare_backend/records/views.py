from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    PatientSerializer,
    DoctorSerializer,
    PatientDoctorMappingSerializer,
    PatientDoctorMappingDetailSerializer,
)

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # detailed serializer for GET and normal serilazier for creating (POST)
        if self.request.method == 'POST':
            return PatientDoctorMappingSerializer
        return PatientDoctorMappingDetailSerializer

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(patient__created_by=self.request.user)


class MappingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        try:
            patient = Patient.objects.get(pk=id, created_by=request.user)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)

        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        doctors = [mapping.doctor for mapping in mappings]
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        try:
            mapping = PatientDoctorMapping.objects.get(pk=id, patient__created_by=request.user)
        except PatientDoctorMapping.DoesNotExist:
            return Response({"error": "Mapping not found."}, status=status.HTTP_404_NOT_FOUND)

        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




















# class MappingDestroyView(generics.DestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = PatientDoctorMapping.objects.all()

#     def get_queryset(self):
#         return super().get_queryset().filter(patient__created_by=self.request.user)

# class PatientDoctorsListView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, patient_id, format=None):
#         try:
#             patient = Patient.objects.get(pk=patient_id, created_by=request.user)
#         except Patient.DoesNotExist:
#             return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)

#         mappings = PatientDoctorMapping.objects.filter(patient=patient)
#         doctors = [mapping.doctor for mapping in mappings]
#         serializer = DoctorSerializer(doctors, many=True)
#         return Response(serializer.data)