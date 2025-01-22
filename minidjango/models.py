from minidjango.db import models


class User(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()

    def __str__(self):
        return self.name
