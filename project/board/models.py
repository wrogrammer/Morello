from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now


class Board(models.Model):
    title = models.CharField(max_length=15, unique=True)
    description = models.CharField(max_length=25)
    category = models.CharField(max_length=20)
    slug = models.SlugField(max_length=15)
    created_at = models.DateField(auto_now_add=True)
    created_at_time = models.TimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('board:board_detail', kwargs={'slug': self.slug, 'board_id': self.pk})

    def __str__(self):
        return self.title


class Card(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title_card = models.CharField(max_length=15)
    description_card = models.CharField(max_length=15)
    colors = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title_card
