from django.contrib import admin
from .models import Board, Card

"""Register models to management in admin panel"""
admin.site.register(Board)
admin.site.register(Card)
