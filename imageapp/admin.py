from django.contrib import admin
from .models import *    # all content of models yha import ho gye


# Register your models here.
#admin wale module me  register krna hai
#yha se admin me kucb bhi register hoga admin pe
admin.site.register(Category)    #categorie  = isliye kyuki admin panel me "s" automatically lag jayega
admin.site.register(Image)

