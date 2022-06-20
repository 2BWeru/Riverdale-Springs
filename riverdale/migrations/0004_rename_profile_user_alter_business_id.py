# Generated by Django 4.0.5 on 2022-06-20 17:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('riverdale', '0003_auto_20220620_1926'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='User',
        ),
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]