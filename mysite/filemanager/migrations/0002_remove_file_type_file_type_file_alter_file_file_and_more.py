# Generated by Django 4.2.4 on 2023-08-23 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='type',
        ),
        migrations.AddField(
            model_name='file',
            name='type_file',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='filemanager.typefile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='typefile',
            name='title',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
