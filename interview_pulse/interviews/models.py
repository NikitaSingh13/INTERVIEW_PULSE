from django.db import models

# Create your models here.
class Interview(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.company}({self.role})"
    
