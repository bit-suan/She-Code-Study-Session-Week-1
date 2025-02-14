from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()  
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
