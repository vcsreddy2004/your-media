from django.db import models
class Posts(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='models/posts/')