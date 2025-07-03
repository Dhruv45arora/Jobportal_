from django.db import models
from Googlelogin.models import CustomUser

class CustomResume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="custom_resume")
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    skilss = models.TextField(max_length=200,blank=True)
    photo = models.ImageField(upload_to='resume/photos/', null=True, blank=True)
    generated_pdf = models.FileField(upload_to='resume/generatedresume/', null=True, blank=True)   

    class Meta:
        db_table = 'custom_resume'