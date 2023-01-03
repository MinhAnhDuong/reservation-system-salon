from django.db import models
from datetime import datetime
from django.utils import timezone

SERVICE_CHOICES = (
    ("ZVOLTE POŽADOVANOU SLUŽBU", "ZVOLTE POŽADOVANOU SLUŽBU"),
    ("MICROPIGMENTACE OBOČÍ", "MICROPIGMENTACE OBOČÍ"),
    ("PERMANENTNÍ MAKE-UP RTŮ", "PERMANENTNÍ MAKE-UP RTŮ"),
    ("LAMINACE ŘAS", "LAMINACE ŘAS"),
    ("PRODLUŽOVÁNÍ ŘAS", "PRODLUŽOVÁNÍ ŘAS"),
)

TIME_CHOICES = [
    ["9:00", "9:00"],
    ["10:00", "10:00"],
    ["11:00", "11:00"],
    ["13:00", "13:00"],
    ["14:00", "14:00"],
    ["15:00", "15:00"],
    ["16:00", "16:00"],
    ["17:00", "17:00"],
]

class BookingSection(models.Model):
    subject = models.CharField(max_length=100, choices=SERVICE_CHOICES,default='ZVOLTE POŽADOVANOU SLUŽBU')
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_mobile = models.CharField(blank=True, null=True, max_length=15)
    date = models.DateField(default=timezone.now)
    time = models.CharField(max_length=50, choices=TIME_CHOICES, default="9:00")
    approved = models.BooleanField(default=False)
