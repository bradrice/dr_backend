# Generated by Django 3.1.3 on 2021-01-11 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carouseltitle', models.CharField(max_length=200)),
                ('artwork', models.ManyToManyField(to='artwork.Artwork')),
            ],
            options={
                'verbose_name': 'Carousel',
                'verbose_name_plural': 'Carousels',
            },
        ),
    ]
