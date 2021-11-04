from forum.models import Disease,Image,Farmer,Crop
from rest_framework import serializers

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Disease
        fields=[
            'diseases',
            'plant',
            'damage',
            'problem'
        ]
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields=[
            'crop_img',
            'posted_at'
        ]
class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Farmer
        fields=[
            'name',
            'location',
            'crop_problem',
            'region'
        ]
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crop
        fields=[
            'crop_name',
            'crop_disease'
        ]
        