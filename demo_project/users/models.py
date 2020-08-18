from django.db import models

# Create your models here.

class Signup(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    email_address = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    confirm_password = models.CharField(max_length = 50)

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    author = models.ForeignKey(Signup, on_delete=models.CASCADE)
    content = models.CharField(max_length=3000)

    def __str__(self):
        return self.title
