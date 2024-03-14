from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


