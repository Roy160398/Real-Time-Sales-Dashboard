# Generated by Django 3.2.5 on 2022-07-20 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesByCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('total_sales', models.FloatField()),
            ],
        ),
    ]