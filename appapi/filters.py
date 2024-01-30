import django_filters
from .models import *
from django_filters import rest_framework as filters



class MarqueVehiculeFilter(django_filters.FilterSet):
    class Meta:
        model = MarqueVehicule
        fields = ['nom', 'pays_origine']

class TypeCarburantFilter(django_filters.FilterSet):
    class Meta:
        model = TypeCarburant
        fields = ['nom', 'description']

class TypeTransmissionFilter(django_filters.FilterSet):
    class Meta:
        model = TypeTransmission
        fields = ['nom', 'description']

class ModeleVehiculeFilter(django_filters.FilterSet):
    class Meta:
        model = ModeleVehicule
        fields = ['nom', 'description']

class CouleurVehiculeFilter(django_filters.FilterSet):
    class Meta:
        model = CouleurVehicule
        fields = ['nom', 'code_hex', 'description']

class OptionVehiculeFilter(django_filters.FilterSet):
    class Meta:
        model = OptionVehicule
        fields = ['nom', 'description']

class NombreDePlaceVehiculeFilter(django_filters.FilterSet):
    class Meta:
        model = NombreDePlaceVehicule
        fields = ['nombre']

class VehiculeFilter(django_filters.FilterSet):
    marquevehicule__nom = django_filters.CharFilter(field_name='marquevehicule__nom', lookup_expr='exact')
    typecarburant__nom = django_filters.CharFilter(field_name='typecarburant__nom', lookup_expr='exact')
    typetransmission__nom = django_filters.CharFilter(field_name='typetransmission__nom', lookup_expr='exact')
    modelevehicule__nom = django_filters.CharFilter(field_name='modelevehicule__nom', lookup_expr='exact')
    couleurvehicule__nom = django_filters.CharFilter(field_name='couleurvehicule__nom', lookup_expr='exact')
    optionvehicule__nom = django_filters.CharFilter(field_name='optionvehicule__nom', lookup_expr='exact')
    nombredeplacevehicule__nom = django_filters.CharFilter(field_name='nombredeplacevehicule__nom', lookup_expr='exact')
    # Add more filters for other related models
    marque__nom = django_filters.CharFilter(marquevehicule__nom='marque__nom', lookup_expr='exact')

    nom = django_filters.CharFilter(field_name='nom', lookup_expr='exact')
    # Add more fields as needed

    class Meta:
        model = Vehicule
        fields = '__all__'  # You can leave it empty or specify the fields you want to include/exclude here


class VenteFilter(django_filters.FilterSet):
    class Meta:
        model = Vente
        fields = ['date_vente', 'prix_vente', 'paiement_effectue']

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = ['date_debut', 'date_fin', 'prix_total', 'est_paye', 'est_livre']

class PromoCodeFilter(django_filters.FilterSet):
    class Meta:
        model = PromoCode
        fields = ['code', 'reduction_percent', 'expiration_date']

class CommentaireLocationFilter(django_filters.FilterSet):
    class Meta:
        model = CommentaireLocation
        fields = ['commentaire', 'note', 'date_creation']

class ContratLocationFilter(django_filters.FilterSet):
    class Meta:
        model = ContratLocation
        fields = ['conditions']

class ContratVenteFilter(django_filters.FilterSet):
    class Meta:
        model = ContratVente
        fields = ['conditions']

class PaiementFilter(django_filters.FilterSet):
    class Meta:
        model = Paiement
        fields = ['date_paiement', 'montant', 'moyen_paiement']

class FactureFilter(django_filters.FilterSet):
    class Meta:
        model = Facture
        fields = ['date_emission', 'montant_total', 'est_payee']

class AgenceLocationFilter(django_filters.FilterSet):
    class Meta:
        model = Service
        fields = ['nom', 'adresse', 'telephone', 'email']

class AssuranceFilter(django_filters.FilterSet):
    class Meta:
        model = Assurance
        fields = ['compagnie', 'numero_police', 'date_debut', 'date_fin']

class StatutLocationFilter(django_filters.FilterSet):
    class Meta:
        model = StatutLocation
        fields = ['nom', 'description']

class StatutVenteFilter(django_filters.FilterSet):
    class Meta:
        model = StatutVente
        fields = ['nom', 'description']

class AvisFilter(django_filters.FilterSet):
    class Meta:
        model = Avis
        fields = ['commentaire', 'note']

class ImageVehiculeFilter(filters.FilterSet):
    image = filters.CharFilter(method='filter_image')

    class Meta:
        model = ImageVehicule
        fields = '__all__'

    def filter_image(self, queryset, name, value):
        return queryset.filter(image__icontains=value)
