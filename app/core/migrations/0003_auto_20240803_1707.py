# Generated by Django 3.2.25 on 2024-08-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_nutrient'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrient',
            name='Considerations',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nutrient',
            name='Daily_Recommended_Intake',
            field=models.TextField(blank=True, null=True),
        ),
    ]
