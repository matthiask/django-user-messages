from django.contrib import admin

from user_messages import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "delivered_at",
        "user",
        "level",
        "message",
        "deliver_once",
    )
    ordering = ["-created_at"]
    raw_id_fields = ("user",)
