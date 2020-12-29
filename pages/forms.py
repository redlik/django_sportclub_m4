from django import forms
from .models import Contact, Member


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name',
                  'email',
                  'subject',
                  'message',
                  ]


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address1', 'address2', 'city',
                  'postcode', 'country',]

