# Generated by Django 3.1.2 on 2020-10-14 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20201014_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'Education'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name_plural': 'Experiences'},
        ),
        migrations.AlterModelOptions(
            name='licensesandcertifications',
            options={'verbose_name_plural': 'Licenses & Certifications'},
        ),
    ]