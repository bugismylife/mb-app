from django.db import models

# Create your models here.

class Posts(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.text[:50]