# Update events/admin.py to match your actual model fields

from django.contrib import admin
from .models import Event, EventUsers

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'date', 'address')  # Event has 'owner' and 'date', not 'created_at'
    search_fields = ('title', 'address', 'description')
    list_filter = ('date',)  # Use 'date' instead of 'created_at'

@admin.register(EventUsers)
class EventUsersAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'event_id', 'rank')  # Correct field names
    search_fields = ('owner_id__email', 'event_id__title')
    list_filter = ('rank',)