from django.db import models


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

