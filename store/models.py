from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
