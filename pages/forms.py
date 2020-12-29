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
        fields = "__all__"

