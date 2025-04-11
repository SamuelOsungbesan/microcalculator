from django.urls import path
from .views import SpecimenListView, SpecimenCreateView, SpecimenDetailView

urlpatterns = [
    path('', SpecimenListView.as_view(), name='calculator-home'),
    path('calculate/', SpecimenCreateView.as_view(), name='calculator-calculate'),
    path('specimen/<int:pk>/', SpecimenDetailView.as_view(), name='calculator-detail'),
]