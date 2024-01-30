# Generated by Django 4.2.7 on 2023-11-14 12:11

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('prenom', models.CharField(max_length=255555, null=True)),
                ('age', models.IntegerField(null=True)),
                ('telephone', models.CharField(max_length=15, null=True)),
                ('sexe', models.CharField(max_length=10, null=True)),
                ('numero_cni', models.CharField(max_length=20, null=True, unique=True)),
                ('numero_permis_conduire', models.CharField(max_length=20, null=True, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos_clients/')),
                ('adresse', models.TextField(null=True)),
                ('pays', models.CharField(max_length=25555, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CouleurVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True, unique=True)),
                ('code_hex', models.CharField(max_length=7, null=True, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raison_location', models.TextField(null=True)),
                ('localisation_utilisateur', models.TextField(null=True)),
                ('localisation_destination', models.TextField(null=True)),
                ('date_vente', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images_vehicules/')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField(null=True)),
                ('date_fin', models.DateTimeField(null=True)),
                ('prix_total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('est_paye', models.BooleanField(default=False, null=True)),
                ('est_livre', models.BooleanField(default=False, null=True)),
                ('paiement_effectue', models.BooleanField(default=False, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.detail')),
            ],
        ),
        migrations.CreateModel(
            name='MarqueVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True, unique=True)),
                ('pays_origine', models.CharField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModeleVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NombreDePlaceVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50000, null=True, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OptionVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, null=True, unique=True)),
                ('reduction_percent', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25555, null=True)),
                ('adresse', models.TextField(null=True)),
                ('telephone', models.CharField(max_length=15555, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCarburant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeTransmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_sortie', models.IntegerField(null=True)),
                ('immatriculation', models.CharField(max_length=20, null=True, unique=True)),
                ('date_vente', models.DateField(null=True)),
                ('boite_vitesse', models.CharField(max_length=2000, null=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('type_carrosserie', models.CharField(max_length=25555, null=True)),
                ('couleur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicules_couleur', to='appapi.couleurvehicule')),
                ('marque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicules_marque', to='appapi.marquevehicule')),
                ('modele', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicules_modele', to='appapi.modelevehicule')),
                ('nombre_places', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicules_nombre_places', to='appapi.nombredeplacevehicule')),
                ('photos', models.ManyToManyField(related_name='vehicle_photos', to='appapi.imagevehicule')),
                ('transmission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicules_transmission', to='appapi.typetransmission')),
                ('type_carburant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicules_carburant', to='appapi.typecarburant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_vente', models.DateTimeField(null=True)),
                ('prix_vente', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('contrat_vente', models.FileField(null=True, upload_to='contrats_vente/')),
                ('paiement_effectue', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to=settings.AUTH_USER_MODEL)),
                ('vehicule', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='StatutVente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(null=True)),
                ('vendu', models.BooleanField(default=False, null=True)),
                ('vente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vente')),
            ],
        ),
        migrations.CreateModel(
            name='StatutLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(null=True)),
                ('rent', models.BooleanField(default=False, null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.location')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paiement', models.DateTimeField(auto_now_add=True, null=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10000, null=True)),
                ('moyen_paiement', models.CharField(max_length=50, null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.location')),
                ('vente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vente')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entree_atelier', models.DateTimeField(null=True)),
                ('date_sortie_atelier', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
                ('est_resolu', models.BooleanField(default=False, null=True)),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vehicule')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='vehicule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vehicule'),
        ),
        migrations.AddField(
            model_name='imagevehicule',
            name='vehicule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vehicule'),
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emission', models.DateTimeField(auto_now_add=True, null=True)),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('est_payee', models.BooleanField(default=False, null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.location')),
            ],
        ),
        migrations.CreateModel(
            name='ContratVente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.TextField(null=True)),
                ('signature_client', models.ImageField(null=True, upload_to='signatures_clients/')),
                ('signature_agence', models.ImageField(null=True, upload_to='signatures_agence/')),
                ('vente', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vente')),
            ],
        ),
        migrations.CreateModel(
            name='ContratLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.TextField(null=True)),
                ('signature_client', models.ImageField(null=True, upload_to='signatures_clients/')),
                ('signature_agence', models.ImageField(null=True, upload_to='signatures_agence/')),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.location')),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField(null=True)),
                ('note', models.PositiveIntegerField(null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.location')),
                ('vente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vente')),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField(null=True)),
                ('note', models.PositiveIntegerField(null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.location')),
                ('vente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vente')),
            ],
        ),
        migrations.CreateModel(
            name='Assurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compagnie', models.CharField(max_length=1000000, null=True)),
                ('numero_police', models.CharField(max_length=10000, null=True)),
                ('date_debut', models.DateField(null=True)),
                ('date_fin', models.DateField(null=True)),
                ('vehicule', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.vehicule')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appapi.service'),
        ),
    ]