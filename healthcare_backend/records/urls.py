from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet,
    DoctorViewSet,
    MappingListCreateView,
    MappingDetailView
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),

    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:id>/', MappingDetailView.as_view(), name='mapping-delete'),
]