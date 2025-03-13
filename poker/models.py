from django.db import models

class Context(models.Model):
    title = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.abbreviation


class StackDepth(models.Model):
    minimum = models.IntegerField()
    maximum = models.IntegerField()

    def __str__(self):
        return f"{self.minimum} - {self.maximum}"
    

class Position(models.Model):
    name = models.CharField(max_length=20, unique=True)
    abbreviation = models.CharField(max_length=5, unique=True)
    description = models.TextField()
    distance_from_button = models.IntegerField()

    def __str__(self):
        return self.name


class RangeEntry(models.Model):
    stack_depth = models.ForeignKey(StackDepth, on_delete=models.CASCADE, null=True)
    context = models.ForeignKey(Context, on_delete=models.CASCADE, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    hand = models.CharField(max_length=5)  # e.g., "AKs", "QJo"
    action = models.CharField(max_length=5, 
                              choices=[('raise', 'Raise'),
                                       ('limp', 'Limp'),
                                       ('n_a', 'n/a')])

    class Meta:
        unique_together = ('position', 'hand', 'stack_depth')  # Avoid duplicate entries

    def __str__(self):
        return f"{self.position.name}/{self.stack} - {self.hand} - {self.action}"
