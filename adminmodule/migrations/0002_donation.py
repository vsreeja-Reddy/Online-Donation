# Generated by Django 5.0.1 on 2024-04-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('message', models.TextField()),
                ('donation_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donation_frequency', models.CharField(choices=[('once', 'Once'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=20)),
            ],
        ),
    ]
