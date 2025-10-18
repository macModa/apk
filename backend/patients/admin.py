from django.contrib import admin
from .models import Patient, Consultation

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("prenom", "nom", "age", "telephone", "derniereVisite", "medecin", "statut")
    search_fields = ("nom", "prenom", "telephone", "medecin")
    list_filter = ("statut",)

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("patient", "date", "motif", "medecin", "statut", "created_at")
    search_fields = ("motif", "medecin", "notes")
    list_filter = ("statut", "date")
