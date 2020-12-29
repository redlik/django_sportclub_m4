from django.contrib import admin
from .models import Contact, Member

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'subject', 'full_name', 'email',
    )

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'status')
    search_fields = ('first_name', 'last_name', 'email', 'date_of_birth',)
    ordering = ('first_name', 'last_name', 'status')