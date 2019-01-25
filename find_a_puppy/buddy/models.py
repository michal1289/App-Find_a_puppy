from django.db import models

# Create your models here.

SIZE = (
    (1, ""),
    (2, "Mały"),
    (3, "Średni"),
    (4, "Duży"),
    (5, "Bardzo duży")
)

CARE = (
    (1, ""),
    (2, "Łatwa"),
    (3, "Średnia"),
    (4, "Trudna")
)

ACTIVITY = (
    (1, ""),
    (2, "Mała aktywności"),
    (3, "Przeciętna aktywność"),
    (4, "Duża aktywności")
)

CHILDREN = (
    (1, ""),
    (2, "Może wychowywać się z dzieckiem"),
    (3, "Nie polecany dla rodziny z dziećmi")
)

CHARACTER = (
    (1, ""),
    (2, "Uległy"),
    (3, "Pośredni"),
    (4, "Lubi dominować")
)

LIVE_IN_CITY = (
    (1, ""),
    (2, "Nadaje się do mieszkania w bloku"),
    (3, "Może mieszkać w bloku z warunkiem możliwości wybiegu"),
    (4, "Tylko dom z ogrodem")
)
SALARY = (
    (1, ""),
    (2, "Stosunkowo małe"),
    (3, "Przeciętne"),
    (4, "Duże")
)

TRAINING = (
    (1, ""),
    (2, "Szybko i chętnie się uczy"),
    (3, "Przeciętne zdolności do uczenia")
)

GUARD = (
    (1, ""),
    (2, "Nie nadaje się"),
    (3, "Nadaje się warunkowo"),
    (4, "Bardzo nadaje się do roli stróża")
)


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    size = models.IntegerField(choices=SIZE)  # wielkość psa
    care = models.IntegerField(choices=CARE)  # pielegnacja sierści
    activity = models.IntegerField(choices=ACTIVITY)  # aktywność fizyczna psa
    children = models.IntegerField(choices=CHILDREN)  # czy odpowiedni dla dzieci
    character = models.IntegerField(choices=CHARACTER)  # charakter
    live_in_city = models.IntegerField(choices=LIVE_IN_CITY)  # # nadaje sie do życia w mieście
    salary = models.IntegerField(choices=SALARY)  # koszty utrzymania
    training = models.IntegerField(choices=TRAINING)  # szkolenie
    guard = models.IntegerField(choices=GUARD)  # czy nadaje się jako stróż

    def __str__(self):
        return f'{self.name}, {self.description}, {self.size}, {self.care}, {self.activity}, {self.children},\
                {self.character}, {self.live_in_city}, {self.salary}, {self.training}. {self.guard}'


class Contact(models.Model):
    title = models.CharField(max_length=128, verbose_name="Tytuł")
    message = models.TextField(verbose_name="Treść")
