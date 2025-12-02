from django.contrib import admin

# Register your models here.
from .models import Event, EventUsers

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_id', 'timestamp', 'address')
    search_fields = ('name', 'address', 'description')
    list_filter = ('timestamp',)

@admin.register(EventUsers)
class EventUsersAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'event_id', 'rank')
    search_fields = ('owner_id__username', 'event_id__name')
    list_filter = ('rank',)
