from django.db import models
from accounts.models import CustomeUser


class Profile(models.Model):
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="users", default="user.jpg")
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.email
