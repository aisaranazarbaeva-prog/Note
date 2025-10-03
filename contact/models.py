from django.db import models
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} ---> {self.phone_number}"

