from django.contrib import admin
from .models import Chat, Message

# Register your models here.
class MessageInline(admin.TabularInline):
    model = Message
    extra = 0


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('title', 'job', 'completed')
    inlines = (MessageInline, )


admin.site.register(Message)



