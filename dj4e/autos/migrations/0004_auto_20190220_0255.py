# Generated by Django 2.1.7 on 2019-02-20 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0003_auto_20190220_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='comments',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='mileage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
