from django.db import models

class UserProfile(models.Model):
    login_name = models.CharField(max_length=150, unique=True)
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    hashed_password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.login_name
