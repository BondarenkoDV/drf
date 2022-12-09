from django.db import models

CHOICES = (
    ('Unresolved', 'Unresolved'),
    ('Resolver', 'Resolved'),
    ('Frozen', 'Frozen')
)


class Tickets(models.Model):
    text = models.CharField(max_length=255)
    status = models.CharField(max_length=10,
                              choices=CHOICES,
                              default='Unresolved')
    feedback = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text

