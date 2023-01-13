# Generated by Django 4.1.3 on 2022-11-28 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtName', models.CharField(max_length=100)),
                ('districtCode', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pradesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pradeshName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phoneNum', models.CharField(max_length=10)),
                ('is_admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Taluka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talukaName', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.state')),
            ],
        ),
        migrations.CreateModel(
            name='Karyakarta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phoneNum', models.CharField(max_length=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.state')),
                ('taluka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.taluka')),
            ],
        ),
        migrations.CreateModel(
            name='BhagatDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtCode', models.CharField(max_length=6)),
                ('dataid', models.CharField(default='', max_length=6)),
                ('entryDate', models.CharField(max_length=15)),
                ('startDate', models.CharField(max_length=15)),
                ('endDate', models.CharField(max_length=15)),
                ('subYear', models.IntegerField()),
                ('name', models.CharField(default='', max_length=100)),
                ('addressOne', models.CharField(max_length=100)),
                ('addressTwo', models.CharField(max_length=100)),
                ('addressThree', models.CharField(max_length=100)),
                ('phoneNum', models.CharField(max_length=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.state')),
                ('taluka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.taluka')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.district'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='taluka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.taluka'),
        ),
    ]