from django.contrib import admin
from .models import *

models_to_register = [
    MarqueVehicule, CustomUser, Vehicule, NombreDePlaceVehicule, Detail, PromoCode,
    CommentaireLocation, ContratLocation, Paiement, Facture, Service,
    Assurance, StatutLocation, Avis, ImageVehicule, Location, Maintenance,
    Vente, TypeCarburant, TypeTransmission, ModeleVehicule, OptionVehicule,
    StatutVente, CouleurVehicule,ContratVente,Publicite
]

for model in models_to_register:
    admin.site.register(model)
