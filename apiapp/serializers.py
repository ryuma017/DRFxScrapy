from rest_framework import serializers

from .models import QuoteItem
class QuoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteItem
        # 出力したいフィールド名をタプルで(括弧とカンマ)で定義します。
        fields = '__all__'