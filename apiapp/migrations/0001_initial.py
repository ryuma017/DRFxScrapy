# Generated by Django 3.2.9 on 2021-11-04 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('author', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=255)),
            ],
        ),
    ]
