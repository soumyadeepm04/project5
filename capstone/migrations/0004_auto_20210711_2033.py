# Generated by Django 3.2.3 on 2021-07-11 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0003_auto_20210711_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='registered',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_event_id', models.IntegerField(null=True)),
                ('registered_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
