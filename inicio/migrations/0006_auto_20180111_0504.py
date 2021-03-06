# Generated by Django 2.0 on 2018-01-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_auto_20180108_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('referrer_email', models.CharField(max_length=200)),
                ('referred_email', models.CharField(max_length=200)),
                ('ref_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RenameModel(
            old_name='Register',
            new_name='Registro',
        ),
    ]
