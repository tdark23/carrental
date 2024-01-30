# urls.py
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/marquevehicule/', MarqueVehiculeViewSet.as_view({'get': 'list', 'post': 'create'}), name='marquevehicule-list'),
    path('api/typecarburant/', TypeCarburantViewSet.as_view({'get': 'list', 'post': 'create'}), name='typecarburant-list'),
    path('api/typetransmission/', TypeTransmissionViewSet.as_view({'get': 'list', 'post': 'create'}), name='typetransmission-list'),
    path('api/modelevehicule/', ModeleVehiculeViewSet.as_view({'get': 'list', 'post': 'create'}), name='modelevehicule-list'),
    path('api/couleurvehicule/', CouleurVehiculeViewSet.as_view({'get': 'list', 'post': 'create'}), name='couleurvehicule-list'),
    path('api/optionvehicule/', OptionVehiculeViewSet.as_view({'get': 'list', 'post': 'create'}), name='optionvehicule-list'),
    path('api/nombredeplacevehicule/', NombreDePlaceVehiculeViewSet.as_view({'get': 'list', 'post': 'create'}), name='nombredeplacevehicule-list'),
    path('vehicules/count/', VehiculeListCountView.as_view(), name='vehicule-list-count'),
    path('api/vehicule/', VehiculeViewSet.as_view({'get': 'list', 'post': 'create'}), name='vehicule-list'),
    path('vehicules/<int:pk>/', VehiculeDetailView.as_view(), name='vehicule-detail'),
    path('add-vehicle/', VehiculeCreateView.as_view(), name='add-vehicle'),
    path('share/<int:vehicle_id>/', create_share_link, name='create-share-link'),
    path('my-vehicles/', UserVehiclesListView.as_view(), name='user-vehicles-list'),
    path('api/vente/', VenteViewSet.as_view({'get': 'list', 'post': 'create'}), name='vente-list'),
    path('api/location/', LocationViewSet.as_view({'get': 'list', 'post': 'create'}), name='location-list'),
    path('api/promocode/', PromoCodeViewSet.as_view({'get': 'list', 'post': 'create'}), name='promocode-list'),
    path('api/commentairelocation/', CommentaireLocationViewSet.as_view({'get': 'list', 'post': 'create'}), name='commentairelocation-list'),
    path('api/contratlocation/', ContratLocationViewSet.as_view({'get': 'list', 'post': 'create'}), name='contratlocation-list'),
    path('api/contratvente/', ContratVenteViewSet.as_view({'get': 'list', 'post': 'create'}), name='contratvente-list'),
    path('api/paiement/', PaiementViewSet.as_view({'get': 'list', 'post': 'create'}), name='paiement-list'),
    path('api/facture/', FactureViewSet.as_view({'get': 'list', 'post': 'create'}), name='facture-list'),
    path('api/service/', ServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='agencelocation-list'),
    path('api/assurance/', AssuranceViewSet.as_view({'get': 'list', 'post': 'create'}), name='assurance-list'),
    path('api/statutlocation/', StatutLocationViewSet.as_view({'get': 'list', 'post': 'create'}), name='statutlocation-list'),
    path('api/statutvente/', StatutVenteViewSet.as_view({'get': 'list', 'post': 'create'}), name='statutvente-list'),
    path('api/avis/', AvisViewSet.as_view({'get': 'list', 'post': 'create'}), name='avis-list'),
    path('api/imagevehicule/', ImageVehiculeViewSet.as_view({'get': 'list', 'post': 'create'}), name='imagevehicule-list'),
    path('api/maintenance/', MaintenanceViewSet.as_view({'get': 'list', 'post': 'create'}), name='maintenance-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('favorites/', FavoriteListView.as_view(), name='favorites-list'),
    path('favorites/details/', FavoriteListDetailView.as_view(), name='favorites-details'),
    path('vehicules-en-vente/', VehiculesEnVenteListView.as_view(), name='vehicules-en-vente'),
    path('vehicules/en-location/', VehiculesEnLocationListView.as_view(), name='vehicules-en-location'),
    path('vehicules/en-location/<int:pk>/', VehiculeLocationDetailView.as_view(), name='vehicule-en-location-detail'),
    path('vehicules/en-vente/<int:pk>/', VehiculeVenteDetailView.as_view(), name='vehicule-en-vente-detail'),
    path('publicites/', PubliciteListView.as_view(), name='publicites-list'),
    path('publicites/<int:pk>/', PubliciteDetailView.as_view(), name='publicite-detail'),
    path('services/list/', ServiceListView.as_view(), name='service-list'),
    path('users/list/', CustomUserListView.as_view(), name='user-list'),
    path('users/service/<str:nom>/', UserListByServiceView.as_view(), name='user-list-by-service'),
    path('users/<str:prenom>/', UserDetailView.as_view(), name='user-detail'),
    path('api/messages/<sender>/<receiver>/', MessageList.as_view(), name='message-list'),
    path('api/chats/', ChatView.as_view(), name='chat-view'),
    path('api/messages/<sender>/<receiver>/', MessageView.as_view(), name='message-view'),
    path('api/send-message/<int:receiver_id>/', SendMessageView.as_view(), name='send-message'),


]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
