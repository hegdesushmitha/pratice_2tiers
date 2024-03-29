# Generated by Django 2.1.12 on 2019-12-18 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('top_name', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('url', models.URLField(unique=True)),
                ('top_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='access_details',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Webpage'),
        ),
    ]
