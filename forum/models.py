from django.db import models
from django.contrib.auth.models import User

class Disease(models.Model):
    mild='mild'
    bad='bad'
    serious='serious'

    Damage_level =[
        (mild,'mild'),
        (bad,'bad'),
        (serious,'serious')
    ]

    foliar_diseases='foliar_diseases'
    stalk_rots='stalk_rots'
    smuts='smuts'
    ear_rots='ear_rots'

    Crop_diseases=[
        (foliar_diseases,'foliar_diseases'),
        (stalk_rots,'stalk_rots'),
        (smuts,'smuts'),
        (ear_rots,'ear_rots'),
    ]
    diseases=models.CharField(choices=Crop_diseases,default='foliar_diseases', max_length=20),
    plant=models.CharField(max_length=20),
    damage=models.CharField(choices=Damage_level, default='mild', max_length=20),
    problem=models.TextField()

class Image(models.Model):
    crop_img=models.ImageField(upload_to='image'),
    posted_at= models.DateField(auto_now_add=True),

    def save_img(self):
         self.save()

class Farmer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    crop_problem=models.TextField()
    region=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

    def save_farmer(self):
        self.save()

class Crop(models.Model):
    crop_disease=models.ForeignKey(Disease, on_delete=models.CASCADE)
    crop_name=models.CharField(max_length=20)

    def __str__(self):
        return self.crop_name

    def save_crop(self):
        self.save()



