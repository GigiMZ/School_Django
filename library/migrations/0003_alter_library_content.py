# Generated by Django 5.1.2 on 2024-10-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_library_content_alter_library_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='content',
            field=models.TextField(),
        ),
    ]
