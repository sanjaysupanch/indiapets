# Generated by Django 3.0.3 on 2020-04-04 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Buffalo', 'Buffalo'), ('Rabbit', 'Rabbit')], max_length=120)),
                ('pet_breed', models.CharField(choices=[('German Shepherd', 'German shepherd'), ('Labrador', 'Labrador'), ('Alaskan', 'Alaskan')], max_length=120)),
                ('pet_image', models.ImageField(upload_to='pets_image/')),
                ('pet_age', models.CharField(max_length=20)),
                ('pet_gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=2)),
                ('pet_price', models.IntegerField()),
                ('pet_description', models.TextField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
