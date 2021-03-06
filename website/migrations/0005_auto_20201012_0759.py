# Generated by Django 3.1.2 on 2020-10-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AddField(
            model_name='order',
            name='zip',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='order',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=90),
        ),
    ]
