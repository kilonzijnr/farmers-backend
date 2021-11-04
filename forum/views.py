from django.shortcuts import render
from forum.models import *
from forum.serializers import *
from rest_framework import viewsets,permissions


class FarmerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Farmer.objects.all()
    serializer_class=FarmerSerializer
    permission_classes=[permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DiseaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Disease.objects.all()
    serializer_class=DiseaseSerializer
    permission_classes=[permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Image.objects.all()
    serializer_class=ImageSerializer
    permission_classes=[permissions.AllowAny]

class CropViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Crop.objects.all()
    serializer_class=CropSerializer
    permission_classes=[permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)