# Generated by Django 4.2.4 on 2023-08-23 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deskription', models.TextField(blank=True, max_length=500, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanager.typefile')),
            ],
        ),
    ]