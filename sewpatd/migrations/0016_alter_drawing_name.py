# Generated by Django 4.0.3 on 2022-03-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sewpatd', '0015_alter_drawing_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='name',
            field=models.CharField(db_index=True, help_text='Unique name (maximum 60 characters)', max_length=60,
                                   verbose_name='Name'),
        ),
    ]
