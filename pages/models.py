from django.db import models
from django_countries.fields import CountryField


class Contact(models.Model):
    full_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=80, null=False, blank=False)
    message = models.TextField()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.subject

class Member(models.Model):
    STATUS_CHOICE = [
        ('CANDIDATE', 'Candidate'),
        ('MEMBER', 'Member'),
    ]
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address1 = models.CharField(max_length=32, null=False, blank=False)
    address2 = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=20, null=False, blank=False)
    county = models.CharField(max_length=32, null=True, blank=True)
    postcode = models.CharField(max_length=8, null=True, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='CANDIDATE')

    def __str__(self):
        self.full_name = self.first_name + " " + self.last_name
        return self.full_name
