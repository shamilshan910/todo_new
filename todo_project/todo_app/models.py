from django.db import models

# Create your models here.
class task_holder(models.Model):
    name=models.CharField(max_length=200)
    priority=models.IntegerField(blank=True)
    date=models.DateField()
    def __str__(self):
        return self.name


