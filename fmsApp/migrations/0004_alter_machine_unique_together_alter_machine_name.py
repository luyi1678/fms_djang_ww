# Generated by Django 4.0.3 on 2023-03-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmsApp', '0003_post_date_mould_machine_category_post_category_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='machine',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]
