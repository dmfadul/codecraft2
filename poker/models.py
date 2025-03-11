from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class RangeEntry(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    hand = models.CharField(max_length=5)  # e.g., "AKs", "QJo"
    action = models.CharField(max_length=5, choices=[('raise', 'Raise'), ('limp', 'Limp')])
    stack = models.IntegerField(default=100)  # Stack size in BBs

    class Meta:
        unique_together = ('position', 'hand', 'stack')  # Avoid duplicate entries

    def __str__(self):
        return f"{self.position.name}/{self.stack} - {self.hand} - {self.action}"
