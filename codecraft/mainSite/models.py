from django.db import models

# Create your models here.


class Message(models.Model):
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_replied = models.BooleanField(default=False)



    def __str__(self):
        return f"{self.user_name} - {self.created_at}"