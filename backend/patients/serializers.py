from rest_framework import serializers
from .models import Patient, Consultation


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    # Accept patient by id on write
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Consultation
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Populate patient object for GET
        data['patient'] = PatientSerializer(instance.patient).data
        return data
