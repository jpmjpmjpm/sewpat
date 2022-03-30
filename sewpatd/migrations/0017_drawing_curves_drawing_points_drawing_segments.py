# Generated by Django 4.0.3 on 2022-03-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sewpatd', '0016_alter_drawing_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawing',
            name='curves',
            field=models.JSONField(blank=True, help_text='Curves in custom JSON format (maximum 100000 bytes)',
                                   max_length=100000, null=True, verbose_name='Curves'),
        ),
        migrations.AddField(
            model_name='drawing',
            name='points',
            field=models.JSONField(blank=True, help_text='Points in custom JSON format (maximum 100000 bytes)',
                                   max_length=100000, null=True, verbose_name='Points'),
        ),
        migrations.AddField(
            model_name='drawing',
            name='segments',
            field=models.JSONField(blank=True, help_text='Segments in custom JSON format (maximum 100000 bytes)',
                                   max_length=100000, null=True, verbose_name='Segments'),
        ),
    ]
