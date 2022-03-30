# Generated by Django 4.0.3 on 2022-03-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sewpatd', '0008_alter_sewingpattern_drawing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='description',
            field=models.CharField(blank=True, help_text='Description (maximum 300 characters)', max_length=300,
                                   verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='name',
            field=models.CharField(db_index=True, help_text='Unique name (maximum 60 characters)', max_length=60,
                                   unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='sewingpattern',
            name='description',
            field=models.CharField(blank=True, help_text='Description (maximum 300 characters)', max_length=300,
                                   verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sewingpattern',
            name='name',
            field=models.CharField(db_index=True, help_text='Unique name (maximum 60 characters)', max_length=60,
                                   unique=True, verbose_name='Name'),
        ),
    ]