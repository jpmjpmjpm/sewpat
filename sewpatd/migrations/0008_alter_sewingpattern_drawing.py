# Generated by Django 4.0.3 on 2022-03-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sewpatd', '0007_alter_drawing_drawing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewingpattern',
            name='drawing',
            field=models.JSONField(blank=True, help_text='JSON representation of the drawing (maximum 100000 bytes)',
                                   max_length=100000, null=True, verbose_name='drawing'),
        ),
    ]
