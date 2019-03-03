# Generated by Django 2.1.7 on 2019-03-01 15:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='incidentImage')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('emergencyLevel', models.IntegerField(blank=True, default=50)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('phone', models.CharField(blank=True, max_length=17)),
            ],
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myServer.User'),
        ),
    ]