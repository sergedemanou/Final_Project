from django.db import models
from django.contrib.auth.models import User
from PIL import Image # pour importer les images avec la librairie pillow
from phone_field import PhoneField
# Create your models here.



class Profile(models.Model):
    PROFILE_CHOICE = (
        ('developpeur', 'developpeur'),
        ('designer', 'designer'),
        ('invité', 'invité')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=300, choices=PROFILE_CHOICE)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    print(phone)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()  #lorsqu'on telecharge une nouvelle image elle va se redimensiooner automatiquement

        img = Image.open(self.image.path)         # ici le redim va respecter les nvlles dimensions prescristes
        if img.height > 300 or img.width > 300 :  # cette method permet de gagner bcp d'espace et ne va pas ralentir l'app
            output_size = (400, 400)
            img.thumbnail(output_size)            # si le fichier image est lourd et large
            img.save(self.image.path)

class Formation(models.Model):

    intitulé = models.CharField(max_length=300)
    établissement = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    date_de_début = models.DateField()
    date_de_fin = models.DateField()
    diplômes_obtenus = models.CharField(max_length=300)
    domaine = models.CharField(max_length=300)
    langages_de_programmation = models.CharField(max_length=300)
    profile_id = models.ForeignKey(Profile, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.intitulé)

class Projets(models.Model):
    intitulé = models.CharField(max_length=300)
    période = models.DateField()
    lien = models.URLField(max_length = 200, null=True)
    profile_id = models.ForeignKey(Profile, related_name='projet', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.intitulé)
