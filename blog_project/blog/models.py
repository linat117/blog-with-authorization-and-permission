from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_publish_post", "Can publish post"),
        ]

    def __str__(self):
        return self.title
