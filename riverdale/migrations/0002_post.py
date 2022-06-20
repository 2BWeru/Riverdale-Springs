# Generated by Django 4.0.5 on 2022-06-20 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riverdale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('name', models.CharField(max_length=50, null=True)),
                ('caption', models.TextField(max_length=50, null=True)),
                ('id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('images', models.ImageField(default='default.jpg', upload_to='photo_images')),
                ('created', models.DateTimeField(auto_now=True)),
                ('neighborhood_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighborhood_post', to='riverdale.neighborhood')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to='riverdale.user')),
            ],
        ),
    ]
