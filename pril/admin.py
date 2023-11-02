from django.contrib import admin

from .models import Pass, Item


@admin.register(Pass)
class PassAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
