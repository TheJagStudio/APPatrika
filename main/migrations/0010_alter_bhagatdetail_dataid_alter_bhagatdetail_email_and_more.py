# Generated by Django 4.1.3 on 2022-12-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_bhagatdetail_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bhagatdetail',
            name='dataid',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='bhagatdetail',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bhagatdetail',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bhagatdetail',
            name='pincode',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='bhagatdetail',
            name='receiptNo',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='bhagatdetail',
            name='remark',
            field=models.CharField(max_length=100),
        ),
    ]
