# Generated by Django 4.1.2 on 2022-10-22 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supers_types', '0001_initial'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='supers_types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supers_types.superstypes'),
        ),
    ]
