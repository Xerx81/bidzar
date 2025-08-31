from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('listings/', views.ListingListCreateView.as_view(), name='listing-list'),
    path('listings/<uuid:pk>/', views.ListingDetailView.as_view(), name='listing-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
