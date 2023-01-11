# Generated by Django 3.2.12 on 2023-01-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_rename_agreementbool_artist_has_agreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='attitude_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='has_agreement',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='professional_rating',
            field=models.IntegerField(default=0),
        ),
    ]