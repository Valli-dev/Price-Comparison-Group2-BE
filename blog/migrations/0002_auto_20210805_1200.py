# Generated by Django 3.2.5 on 2021-08-05 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210805_1200'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ManyToManyField(blank=True, related_name='likebutton', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
