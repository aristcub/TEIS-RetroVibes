from django.urls import path
from .views import HomePageView, OptionsView, VinylIndexView, VinylShowView, CartView, CartRemoveAllView, VinylCreateView, VinylForm
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('options/', OptionsView.as_view(), name='index'),
    path('vinyls/', VinylIndexView.as_view(), name="vinyl_list"),
    path('vinyls/<str:id>', VinylShowView.as_view(), name='show'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<int:vinyl_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('vinyls/create/', VinylCreateView.as_view(), name='vinyl_create'),  # URL para crear un vinilo
    
]