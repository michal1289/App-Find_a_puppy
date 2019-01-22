from django.db import models

# Create your models here.


class RaceList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    size = models.CharField(max_length=255, null=True)  # wielkość psa
    care = models.CharField(max_length=255, null=True)  # pielegnacja
    activity = models.CharField(max_length=255, null=True)  # aktywność
    children = models.CharField(max_length=64, null=True)  # czy odpowiedni dla dzieci
    character = models.CharField(max_length=255, null=True)  # charakter
    live_in_city = models.CharField(max_length=255, null=True)  # # nadaje sie do życia w mieście
    salary = models.CharField(max_length=64, null=True)  # koszty utrzymania
    training = models.CharField(max_length=64, null=True)  # szkolenie
    save = models.CharField(max_length=64, null=True)  # czy nadaje się jako stróż

    def __str__(self):
        return f'{self.name}, \t{self.description}'
