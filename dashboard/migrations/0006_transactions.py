# Generated by Django 3.2.15 on 2022-08-26 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_suscriptions_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('btc_address', models.CharField(default=None, max_length=200)),
                ('amount', models.FloatField(default=None)),
                ('transactions_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_hash', models.TextField(default=None, null=True)),
                ('confirmation', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('suscriptions', models.ManyToManyField(to='dashboard.suscriptions')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
