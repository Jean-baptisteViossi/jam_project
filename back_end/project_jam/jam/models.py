from django.db import models

class HistoirePartagee(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()

class Mission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class Histoire(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_partage = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
