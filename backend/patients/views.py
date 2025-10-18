from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Patient, Consultation
from .serializers import PatientSerializer, ConsultationSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('nom', 'prenom')
    serializer_class = PatientSerializer


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.select_related('patient').all().order_by('-date')
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        patient_id = self.request.query_params.get('patient')
        statut = self.request.query_params.get('statut')
        if patient_id:
            qs = qs.filter(patient__id=patient_id)
        if statut:
            qs = qs.filter(statut=statut)
        return qs

    def create(self, request, *args, **kwargs):
        # Ensure patient exists
        patient_id = request.data.get('patient')
        if not patient_id:
            return Response({'detail': 'patient is required'}, status=status.HTTP_400_BAD_REQUEST)
        get_object_or_404(Patient, pk=patient_id)
        return super().create(request, *args, **kwargs)
