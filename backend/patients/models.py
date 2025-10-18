from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    age = models.IntegerField()
    telephone = models.CharField(max_length=50)
    derniereVisite = models.DateField()
    medecin = models.CharField(max_length=150)
    statut = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations')
    date = models.DateField()
    motif = models.CharField(max_length=255)
    traitement = models.CharField(max_length=255, blank=True, null=True)
    medecin = models.CharField(max_length=150)
    notes = models.TextField(blank=True, null=True)
    statut = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consultation {self.date} - {self.patient}"
