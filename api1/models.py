from django.db import models

# Create your models here.


class Tutorial2(models.Model):
    tutorialNo = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    StartDate = models.DateField(auto_now_add=True)


def __str__(self):
    return self.title

