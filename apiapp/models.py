from django.db import models

# Create your models here.
class QuoteItem(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiapp_quoteitem'