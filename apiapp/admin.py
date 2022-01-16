from django.contrib import admin

# 以下を追加します。
from .models import QuoteItem
@admin.register(QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    pass