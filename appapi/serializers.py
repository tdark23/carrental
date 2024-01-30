# serializers.py
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'prenom', 'age', 'telephone', 'sexe', 'numero_cni', 'numero_permis_conduire', 'photo', 'adresse', 'pays', 'user_type', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class MarqueVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarqueVehicule
        fields = '__all__'

class TypeCarburantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCarburant
        fields = '__all__'

class TypeTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeTransmission
        fields = '__all__'

class ModeleVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeleVehicule
        fields = '__all__'

class CouleurVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouleurVehicule
        fields = '__all__'

class OptionVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionVehicule
        fields = '__all__'

class NombreDePlaceVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NombreDePlaceVehicule
        fields = '__all__'

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'

class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = '__all__'

class CommentaireLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireLocation
        fields = '__all__'

class ContratLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratLocation
        fields = '__all__'

class ContratVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratVente
        fields = '__all__'

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'

class AssuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assurance
        fields = '__all__'

class StatutLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutLocation
        fields = '__all__'

class StatutVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutVente
        fields = '__all__'

class AvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'

class ImageVehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageVehicule
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'

class FavoriteListSerializer(serializers.ModelSerializer):
    vehicles = VehiculeSerializer(many=True, read_only=True)

    class Meta:
        model = FavoriteList
        fields = ['vehicles']

class AddToFavoriteSerializer(serializers.Serializer):
    vehicule_id = serializers.IntegerField()

class RemoveFromFavoriteSerializer(serializers.Serializer):
    vehicule_id = serializers.IntegerField()

class FavoriteListDetailSerializer(serializers.Serializer):
    vehicles = VehiculeSerializer(many=True, read_only=True)

class VehiculeDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer(many=True, read_only=True)
    vente = VenteSerializer(many=True, read_only=True)


    class Meta:
        model = Vehicule
        fields = '__all__'

class PubliciteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicite
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceDetailSerializer(serializers.ModelSerializer):
    utilisateurs = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['nom', 'utilisateurs']

class CustomUserSerializer(serializers.ModelSerializer):
    user_type_details = ServiceSerializer(source='user_type', read_only=True)
    vehicles = VehiculeSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
