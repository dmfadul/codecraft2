from django.db import models

class Context(models.Model):
    title = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.abbreviation
    

class Position(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class RangeEntry(models.Model):
    stack = models.IntegerField(default=100)  # Stack size in BBs
    # context = models.ForeignKey(Context, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    hand = models.CharField(max_length=5)  # e.g., "AKs", "QJo"
    action = models.CharField(max_length=5, choices=[('raise', 'Raise'), ('limp', 'Limp')])

    class Meta:
        unique_together = ('position', 'hand', 'stack')  # Avoid duplicate entries

    def __str__(self):
        return f"{self.position.name}/{self.stack} - {self.hand} - {self.action}"
