#admin panel me add yhi se hoga kuch bhi and track bhi
from django.db import models

# Create your models here.

#create categories model
#categorie  = isliye kyuki admin panel me "s" automatically lag jayega
class Category(models.Model): #models ki sari properties isme aa jayegi
    title=models.CharField(max_length=100)    #title
    description=models.TextField()    #description


    def __str__(self):    #iske bina likhega    category1 category2 likhega
        return self.title   #title ka naam likhega

#create image model
class Image(models.Model):
    title=models.CharField(max_length=200)   #image ka title
    description=models.TextField()     #image ka description
    image=models.ImageField(upload_to='images')   # actual image and folder ka naaam 'images'
    added_date=models.DateTimeField()   # kab add ki gyi hai photo
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)   # photo ki category    #categorys  = isliye kyuki admin panel me "s" automatically lag jayega


    def __str__(self):    #iske bina likhega    categoryobject1 categoryobject2 likhega
        return self.title   #title ka naam likhega
