# Generated by Django 4.0.3 on 2022-03-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sewpatd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewingpattern',
            name='name',
            field=models.CharField(db_index=True, help_text='Unique name (maximum 60 SLUG characters)', max_length=60,
                                   unique=True, verbose_name='Name'),
        ),
    ]
