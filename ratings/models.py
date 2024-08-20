from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_rating')
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5star')))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'profile']

    def __str__(self):
        return f'{self.owner} rated {self.profile} {self.rating} stars'