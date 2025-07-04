# Generated by Django 5.2.3 on 2025-06-26 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Googlelogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
