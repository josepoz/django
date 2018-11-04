# Generated by Django 2.0.9 on 2018-11-04 02:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
