# Generated by Django 4.0.3 on 2022-03-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sewpatd', '0002_alter_sewingpattern_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewingpattern',
            name='drawing',
            field=models.JSONField(blank=True, help_text='JSON representation of the drawing', max_length=100000,
                                   null=True, verbose_name='drawing'),
        ),
    ]