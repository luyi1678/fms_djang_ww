# Generated by Django 4.0.3 on 2023-04-06 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmsApp', '0007_material_post_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='material',
        ),
        migrations.AddField(
            model_name='post',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fmsApp.material'),
        ),
    ]
