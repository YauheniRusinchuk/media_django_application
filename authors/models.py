from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.avatar)


    def fullname(self):
    	result = self.user.first_name.replace(" ","") + self.user.last_name.replace(" ", "")
    	return result


    class Meta:
        verbose_name = "Profile"
