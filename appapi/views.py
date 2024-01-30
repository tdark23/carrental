
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate
from .filters import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.db.models import Count
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Message
from .serializers import MessageSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import Http404

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()

        # Rendu du modèle HTML
        subject = 'Bienvenue sur la plateforme'
        html_message = render_to_string('welcome_email.html', {'username': user.prenom, 'user_type': user.user_type})

        # Rendu du modèle de texte brut pour le contenu alternatif
        text_message = strip_tags(html_message)

        from_email = 'lamboarmand28@gmail.com'  # Mettez votre adresse e-mail
        recipient_list = [user.email]

        # Envoyer l'e-mail avec contenu HTML et texte brut
        email = EmailMultiAlternatives(subject, text_message, from_email, recipient_list)
        email.attach_alternative(html_message, 'text/html')
        email.send()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data)
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class BaseCreateListViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MarqueVehiculeViewSet(BaseCreateListViewSet):
    queryset = MarqueVehicule.objects.all()
    serializer_class = MarqueVehiculeSerializer
    filter_class = MarqueVehiculeFilter    

class TypeCarburantViewSet(BaseCreateListViewSet):
    queryset = TypeCarburant.objects.all()
    serializer_class = TypeCarburantSerializer
    filter_class = TypeCarburantFilter

class TypeTransmissionViewSet(BaseCreateListViewSet):
    queryset = TypeTransmission.objects.all()
    serializer_class = TypeTransmissionSerializer
    filter_class = TypeTransmissionFilter

class ModeleVehiculeViewSet(BaseCreateListViewSet):
    queryset = ModeleVehicule.objects.all()
    serializer_class = ModeleVehiculeSerializer
    filter_class = ModeleVehiculeFilter

class CouleurVehiculeViewSet(BaseCreateListViewSet):
    queryset = CouleurVehicule.objects.all()
    serializer_class = CouleurVehiculeSerializer
    filter_class = CouleurVehiculeFilter

class OptionVehiculeViewSet(BaseCreateListViewSet):
    queryset = OptionVehicule.objects.all()
    serializer_class = OptionVehiculeSerializer
    filter_class = OptionVehiculeFilter

class NombreDePlaceVehiculeViewSet(BaseCreateListViewSet):
    queryset = NombreDePlaceVehicule.objects.all()
    serializer_class = NombreDePlaceVehiculeSerializer
    filter_class = NombreDePlaceVehiculeFilter

class VehiculeViewSet(BaseCreateListViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer
    filter_class = VehiculeFilter

    def get_queryset(self):
        queryset = super().get_queryset()

        # Custom filtering based on query parameters
        marque_nom = self.request.query_params.get('marquevehicule__nom', None)
        if marque_nom:
            queryset = queryset.filter(marquevehicule__nom=marque_nom)

        # Additional custom filtering based on other conditions
        # ...

        return queryset
    

class VenteViewSet(BaseCreateListViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer
    filter_class = VenteFilter

class LocationViewSet(BaseCreateListViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_class = LocationFilter

class PromoCodeViewSet(BaseCreateListViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
    filter_class = PromoCodeFilter

class CommentaireLocationViewSet(BaseCreateListViewSet):
    queryset = CommentaireLocation.objects.all()
    serializer_class = CommentaireLocationSerializer
    filter_class = CommentaireLocationFilter

class ContratLocationViewSet(BaseCreateListViewSet):
    queryset = ContratLocation.objects.all()
    serializer_class = ContratLocationSerializer
    filter_class = ContratLocationFilter

class ContratVenteViewSet(BaseCreateListViewSet):
    queryset = ContratVente.objects.all()
    serializer_class = ContratVenteSerializer
    filter_class = ContratVenteFilter

class PaiementViewSet(BaseCreateListViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

class FactureViewSet(BaseCreateListViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class ServiceViewSet(BaseCreateListViewSet):
    queryset = Service.objects.all()
    serializer_class = AgenceSerializer
    filter_class = AgenceLocationFilter

class VehiculeCreateView(generics.CreateAPIView):
    serializer_class = VehiculeSerializer
    permission_classes = (permissions.IsAuthenticated,)  # You may adjust permissions as needed

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assuming you want to associate the vehicle with the current user


class AssuranceViewSet(BaseCreateListViewSet):
    queryset = Assurance.objects.all()
    serializer_class = AssuranceSerializer
    filter_class = AssuranceFilter


class StatutLocationViewSet(BaseCreateListViewSet):
    queryset = StatutLocation.objects.all()
    serializer_class = StatutLocationSerializer
    filter_class = StatutLocationFilter


class StatutVenteViewSet(BaseCreateListViewSet):
    queryset = StatutVente.objects.all()
    serializer_class = StatutVenteSerializer
    filter_class = StatutVenteFilter


class AvisViewSet(BaseCreateListViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer
    filter_class = AvisFilter


class ImageVehiculeViewSet(BaseCreateListViewSet):
    queryset = ImageVehicule.objects.all()
    serializer_class = ImageVehiculeSerializer
    filter_class = ImageVehiculeFilter


class MaintenanceViewSet(BaseCreateListViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class UserVehiclesListView(generics.ListAPIView):
    serializer_class = VehiculeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        if user.user_type and user.user_type.nom == 'particulier':
            # Show vehicles added by individual customers
            return Vehicule.objects.filter(user=user)
        elif user.user_type and user.user_type.nom == 'agence':
            # Show vehicles added by agencies
            return Vehicule.objects.filter(user=user)
        else:
            # Default case (adjust as needed)
            return Vehicule.objects.none()

class FavoriteListView(generics.RetrieveUpdateAPIView):
    serializer_class = FavoriteListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        favorite_list, created = FavoriteList.objects.get_or_create(user=user)
        return favorite_list

    def post(self, request, *args, **kwargs):
        serializer = AddToFavoriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicule_id = serializer.validated_data['vehicule_id']
        vehicule = Vehicule.objects.get(pk=vehicule_id)

        favorite_list = self.get_object()
        favorite_list.vehicles.add(vehicule)

        return Response({'detail': 'Véhicule ajouté aux favoris.'}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        serializer = RemoveFromFavoriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicule_id = serializer.validated_data['vehicule_id']
        vehicule = Vehicule.objects.get(pk=vehicule_id)

        favorite_list = self.get_object()
        favorite_list.vehicles.remove(vehicule)

        return Response({'detail': 'Véhicule retiré des favoris.'}, status=status.HTTP_204_NO_CONTENT)


class FavoriteListDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = FavoriteListDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        favorite_list, created = FavoriteList.objects.get_or_create(user=user)
        return favorite_list

    def post(self, request, *args, **kwargs):
        serializer = AddToFavoriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicule_id = serializer.validated_data['vehicule_id']
        vehicule = Vehicule.objects.get(pk=vehicule_id)

        favorite_list = self.get_object()
        favorite_list.vehicles.add(vehicule)

        return Response({'detail': 'Véhicule ajouté aux favoris.'}, status=status.HTTP_201_CREATED)

class VehiculesEnVenteListView(generics.ListAPIView):
    serializer_class = VehiculeSerializer

    def get_queryset(self):
        # Récupérer les IDs des véhicules vendus
        vehicules_vendus_ids = Vente.objects.values_list('vehicule_id', flat=True)

        # Filtrer les véhicules qui ne sont pas vendus
        return Vehicule.objects.filter(en_vente=True).exclude(id__in=vehicules_vendus_ids)

class VehiculeDetailView(generics.RetrieveAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeDetailSerializer


class VehiculesEnLocationListView(generics.ListAPIView):
    serializer_class = VehiculeSerializer

    def get_queryset(self):
        # Filtrer les véhicules qui sont actuellement en location
        return Vehicule.objects.filter(en_location=True)

class VehiculeLocationDetailView(generics.RetrieveAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeDetailSerializer

class VehiculeVenteDetailView(generics.RetrieveAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeDetailSerializer


class PubliciteListView(generics.ListCreateAPIView):
    serializer_class = PubliciteSerializer

    def get_queryset(self):
        now = timezone.now()
        return Publicite.objects.filter(date_debut__lte=now, date_fin__gte=now)

class PubliciteDetailView(generics.RetrieveAPIView):
    queryset = Publicite.objects.all()
    serializer_class = PubliciteSerializer

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserListByServiceView(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        service_nom = self.kwargs['nom']  # Obtenez le nom du service à partir des paramètres d'URL
        return CustomUser.objects.filter(user_type__nom=service_nom)

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'prenom'  # Utilisez le champ correct pour la recherche

@api_view(['POST'])
def create_share_link(request, vehicle_id):
    try:
        vehicle = Vehicule.objects.get(id=vehicle_id)
    except Vehicule.DoesNotExist:
        return Response({"error": "Vehicule not found"}, status=404)

    # Générez ici le lien de partage ou effectuez toute autre logique de partage
    share_link = f"https://example.com/share/{vehicle_id}"

    return Response({"share_link": share_link}, status=200)

class VehiculeListCountView(generics.ListAPIView):
    serializer_class = VehiculeSerializer

    def get_queryset(self):
        queryset = Vehicule.objects.all()
        filter_params = self.request.query_params

        # Utilisez votre filtre personnalisé pour filtrer les résultats
        filtered_queryset = VehiculeFilter(filter_params, queryset).qs

        # Utilisez la méthode annotate pour compter le nombre de chaque élément
        annotated_queryset = filtered_queryset.values('marque', 'type_carburant', 'transmission', 'modele', 'couleur', 'option', 'nombre_places').annotate(
            count=Count('id')
        )

        return annotated_queryset


class MessageList(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, sender=None, receiver=None):
        try:
            sender_id = int(sender)
            receiver_id = int(receiver)
        except ValueError:
            return Response({"error": "Invalid sender or receiver ID"}, status=status.HTTP_400_BAD_REQUEST)

        messages = Message.objects.filter(sender_id=sender_id, receiver_id=receiver_id, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return Response(serializer.data)

    def post(self, request, sender=None, receiver=None):
        sender_user = get_object_or_404(get_user_model(), id=sender)
        receiver_user = get_object_or_404(get_user_model(), id=receiver)

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=sender_user, receiver=receiver_user)
            self.send_message(serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def send_message(self, message):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_group',
            {
                'type': 'chat.message',
                'message': MessageSerializer(message).data
            }
        )


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.exclude(username=request.user.username)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, sender, receiver):
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver) | \
                   Message.objects.filter(sender_id=receiver, receiver_id=sender)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class SendMessageView(APIView):
    def post(self, request, receiver_id):
        sender = request.user  # L'utilisateur qui envoie le message
        receiver = get_user_model().objects.get(pk=receiver_id)

        # Assurez-vous que le receiver existe
        if not receiver:
            return Response({"error": "Receiver not found"}, status=status.HTTP_404_NOT_FOUND)

        # Récupérez le contenu du message à partir des données de la requête
        content = request.data.get('content', '')

        # Créez le message
        message = Message.objects.create(sender=sender, receiver=receiver, content=content)

        # Sérialisez le message pour l'inclure dans la réponse
        serializer = MessageSerializer(message)

        return Response(serializer.data, status=status.HTTP_201_CREATED)