from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.





class Profile (models.Model):

    ROLE = (
        ('etudiant', 'Etudiant'),
        ('enseignant', 'Enseignant'),
        ('moderateur','Moderateur')
    )

    PROMO = (
        ('1cpi', '1CPI'),
        ('2cpi', '2CPI'),
        ('1cs', '1CS'),
        ('2cs', '2CS'),
        ('3cs', '3CS'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_naissance = models.DateField()
    numero_telephone = models.IntegerField()
    role = models.CharField(choices=ROLE,default='etudiant',max_length=10)
    promotion = models.CharField(choices=PROMO,default='1cpi',max_length=3)
    bio = models.TextField()
    slug = models.SlugField(max_length=250,unique =True)

    def get_absolute_url(self):
        return reverse('Esi_Forum:Main',
        args=[self.role,
              self.user.username,
              self.slug])

    def __str__(self):
        return 'le nom : {} et le prénom : {}'.format(self.user.username,self.user.lastname)


class Publication(models.Model) :

    date_de_publication = models.DateField(auto_now_add=True)
    date_de_modification= models.DateField(auto_now=True)
    section = models.CharField(max_length=30)
    text = models.TextField()
    upvote = models.IntegerField()
    titre = models.CharField(max_length=30)
    lauteur = models.ForeignKey(User,on_delete=models.CASCADE,related_name='publications')
    ''' photo = models.ImageField() '''

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ('-upvote',)

class Commentaire(models.Model):

    date_de_commentaire = models.ForeignKey(Publication,on_delete =models.CASCADE,related_name="commentaires",related_query_name="commentaire")
    text = models.TextField()
    upvote = models.IntegerField()
    

    def __str__(self):
        return self.pk


'''class Publication_enrigistre(models.Model):
    idpe = models.IntegerField(primary_key=True)
    idu = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)

    def __str__(self):
        return self.idpe 

class Publication_archivee(models.Model):
    idpa =models.IntegerField(primary_key=True)

    def __str__(self):
        return self.idpa 

class Fichier_attachee (models.Model):
    idfa = models.IntegerField(primary_key=True)
    idp = models.ForeignKey(Publication,on_delete=models.CASCADE)
    idc = models.ForeignKey(Commentaire,on_delete=models.CASCADE)

    def __str__(self):
        return self.idfa ''' 

class Statistiques (models.Model):
    ids = models.IntegerField(primary_key=True)
    nmbr_publication = models.IntegerField()
    nmbr_commentaires = models.IntegerField()
    upvote = models.IntegerField()

    def __str__(self):
        return self.ids