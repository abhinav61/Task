from django.db import models


# Create your models here.
class Data(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name,self.last_name,self.company_name,self.email_id,self.phone_number,self.password,self.confirm_password} Data'
    
    def save(self):
        super.().save()
        