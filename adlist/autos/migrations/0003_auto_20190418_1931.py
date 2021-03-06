# Generated by Django 2.1.7 on 2019-04-18 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autos', '0002_auto_20190418_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.Auto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_autos', through='autos.FavAuto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='favauto',
            unique_together={('auto', 'user')},
        ),
    ]
