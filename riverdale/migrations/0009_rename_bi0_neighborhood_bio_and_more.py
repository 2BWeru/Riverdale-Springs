# Generated by Django 4.0.5 on 2022-06-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riverdale', '0008_alter_user_neighborhood_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='bi0',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='testimonials',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
