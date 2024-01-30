
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils import timezone

class MarqueVehicule(models.Model):
    nom = models.CharField(max_length=50, unique=True,null=True)
    pays_origine = models.CharField(max_length=5000,null=True)

    def __str__(self):
        return f'Marque: {self.nom} - Pays : {self.pays_origine}'

class TypeCarburant(models.Model):
    nom = models.CharField(max_length=50, unique=True,null=True)
    description = models.TextField(null=True)

class TypeTransmission(models.Model):
    nom = models.CharField(max_length=50, unique=True,null=True)
    description = models.TextField(null=True)

class ModeleVehicule(models.Model):
    nom = models.CharField(max_length=50, unique=True,null=True)
    description = models.TextField(null=True)

class CouleurVehicule(models.Model):
    nom = models.CharField(max_length=50, unique=True,null=True)
    code_hex = models.CharField(max_length=7, unique=True,null=True)
    description = models.TextField(null=True)

class OptionVehicule(models.Model):
    nom = models.CharField(max_length=50, unique=True,null=True)
    description = models.TextField(null=True)

class NombreDePlaceVehicule(models.Model):
    nombre = models.IntegerField(null=True)

class Service(models.Model):
    nom = models.CharField(max_length=25555,null=True)
    adresse = models.TextField(null=True)
    telephone = models.CharField(max_length=15555,null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.nom}"


class CustomUser(AbstractUser):
    # Champs supplémentaires du client
    prenom = models.CharField(max_length=255555,null=True)
    age = models.IntegerField(null=True)
    telephone = models.CharField(max_length=15,null=True)
    sexe = models.CharField(max_length=10,null=True)
    numero_cni = models.CharField(max_length=20, unique=True,null=True)
    numero_permis_conduire = models.CharField(max_length=20, unique=True,null=True)
    photo = models.ImageField(upload_to='medias/photos_clients/', null=True, blank=True)
    adresse = models.TextField(null=True)
    pays = models.CharField(max_length=25555,null=True)
    user_type = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.prenom}"

class Vehicule(models.Model):
    marque = models.ForeignKey(MarqueVehicule, on_delete=models.CASCADE, null=True, related_name='vehicules_marque')
    annee_sortie = models.IntegerField(null=True)
    immatriculation = models.CharField(max_length=20, unique=True, null=True)
    date_vente = models.DateField(null=True)
    boite_vitesse = models.CharField(max_length=2000, null=True)
    modele = models.ForeignKey(ModeleVehicule, on_delete=models.CASCADE, null=True, related_name='vehicules_modele')
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    transmission = models.ForeignKey(TypeTransmission, on_delete=models.CASCADE, null=True, related_name='vehicules_transmission')
    type_carrosserie = models.CharField(max_length=25555, null=True)
    type_carburant = models.ForeignKey(TypeCarburant, on_delete=models.CASCADE, null=True, related_name='vehicules_carburant')
    couleur = models.ForeignKey(CouleurVehicule, on_delete=models.CASCADE, null=True, related_name='vehicules_couleur')
    nombre_places = models.ForeignKey(NombreDePlaceVehicule, on_delete=models.CASCADE, null=True, related_name='vehicules_nombre_places')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='vehicles')
    en_vente = models.BooleanField(default=True)
    en_location = models.BooleanField(default=False)
    photos = models.ManyToManyField('ImageVehicule', related_name='vehicle_photos')

    def __str__(self):
        return f'Resultat de {self.marque.nom}'


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), related_name='sent_messages', on_delete=models.CASCADE ,null=True)
    receiver = models.ForeignKey(get_user_model(), related_name='received_messages', on_delete=models.CASCADE ,null=True)
    content = models.TextField(null=True)
    is_read = models.BooleanField(default=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"De {self.sender.prenom} à {self.receiver.prenom}: {self.content}"

    class Meta:
        ordering = ('created_at',)


class FavoriteList(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='favorite_list')
    vehicles = models.ManyToManyField('Vehicule', related_name='favorited_by')


class Vente(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='sales')
    date_vente = models.DateTimeField(null=True)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    contrat_vente = models.FileField(upload_to='contrats_vente/',null=True)
    paiement_effectue = models.BooleanField(default=False,null=True)


class Detail(models.Model):
    raison_location = models.TextField(null=True)
    localisation_utilisateur = models.TextField(null=True)
    localisation_destination = models.TextField(null=True)
    date_vente = models.DateField(null=True)

class Location(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE,null=True)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    date_debut = models.DateTimeField(null=True)
    date_fin = models.DateTimeField(null=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    est_paye = models.BooleanField(default=False,null=True)
    est_livre = models.BooleanField(default=False,null=True)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE,null=True)
    paiement_effectue = models.BooleanField(default=False,null=True)

class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True,null=True)
    reduction_percent = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    expiration_date = models.DateField()

class CommentaireLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    commentaire = models.TextField(null=True)
    note = models.PositiveIntegerField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE,null=True)


class ContratLocation(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE,null=True)
    conditions = models.TextField(null=True)
    signature_client = models.ImageField(upload_to='signatures_clients/',null=True)
    signature_agence = models.ImageField(upload_to='signatures_agence/',null=True)

class ContratVente(models.Model):
    vente = models.OneToOneField(Vente, on_delete=models.CASCADE,null=True)
    conditions = models.TextField(null=True)
    signature_client = models.ImageField(upload_to='signatures_clients/',null=True)
    signature_agence = models.ImageField(upload_to='signatures_agence/',null=True)

class Paiement(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    date_paiement = models.DateTimeField(auto_now_add=True,null=True)
    montant = models.DecimalField(max_digits=10000, decimal_places=2,null=True)
    moyen_paiement = models.CharField(max_length=50,null=True)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE,null=True)

class Facture(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    date_emission = models.DateTimeField(auto_now_add=True,null=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    est_payee = models.BooleanField(default=False,null=True)

class Assurance(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,null=True)
    compagnie = models.CharField(max_length=1000000,null=True)
    numero_police = models.CharField(max_length=10000,null=True)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)

class StatutLocation(models.Model):
    nom = models.CharField(max_length=50, unique=True,null=True)
    description = models.TextField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    rent = models.BooleanField(default=False,null=True)


class StatutVente(models.Model):
    nom = models.CharField(max_length=50, unique=True,null=True)
    description = models.TextField(null=True)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE,null=True)
    vendu = models.BooleanField(default=False,null=True)


class Avis(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    commentaire = models.TextField(null=True)
    note = models.PositiveIntegerField(null=True)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE,null=True)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)


class ImageVehicule(models.Model):
    image = models.ImageField(upload_to='medias/images_vehicule/',null=True)


class Maintenance(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE,null=True)
    date_entree_atelier = models.DateTimeField(null=True)
    date_sortie_atelier = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    est_resolu = models.BooleanField(default=False,null=True)

class Publicite(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='publicites/', null=True, blank=True)
    vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    createur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    est_en_vente = models.BooleanField(default=True)

    def clean(self):
        # Vérification que la date de début est antérieure à la date de fin
        if self.date_debut >= self.date_fin:
            raise ValidationError("La date de début doit être antérieure à la date de fin.")

        # Vérification que la date de fin est postérieure à la date actuelle
        if self.date_fin <= timezone.now():
            raise ValidationError("La date de fin doit être postérieure à la date actuelle.")

    def __str__(self):
        return self.titre

