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

    class meta:
        unique_together = ('minimum', 'maximum')

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
        return f"{self.position.name}/{self.stack_depth} - {self.hand} - {self.action}"

    @classmethod
    def gen_range(cls, position, stack_depth, context):
        ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]       
        hands = [
            f"{r1}{r2}o" if i < j else f"{r2}{r1}s" if i > j else f"{r1}{r2}"
            for i, r1 in enumerate(ranks) for j, r2 in enumerate(ranks)
        ]

        new_entries = [
            cls(position=position, stack_depth=stack_depth, context=context, hand=hand, action='fold')
            for hand in hands
        ]

        if new_entries:
            cls.objects.bulk_create(new_entries)

        return 0
