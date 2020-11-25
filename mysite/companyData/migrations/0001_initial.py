# Generated by Django 2.2.4 on 2020-11-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
                ('companystockCode', models.CharField(max_length=200)),
                ('companyBuz', models.TextField()),
                ('companyProd', models.TextField()),
                ('companyListStartDate', models.CharField(max_length=200)),
                ('companyCEO', models.CharField(max_length=200)),
                ('companySite', models.CharField(max_length=200)),
                ('companyLocal', models.CharField(max_length=200)),
            ],
        ),
    ]
