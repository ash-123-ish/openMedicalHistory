# Generated by Django 3.0.5 on 2020-04-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=200)),
                ('Aadhar_Number', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=200)),
                ('Age', models.IntegerField(default=0)),
                ('Sex', models.CharField(max_length=5)),
                ('Phone_number', models.CharField(max_length=10)),
                ('Bill_no', models.IntegerField(unique=True)),
                ('CR_no', models.IntegerField()),
                ('Report', models.ImageField(blank=True, max_length=255, null=True, upload_to='report/%Y/%m/%d/')),
                ('Test_name', models.CharField(max_length=200)),
                ('Medlab_name', models.CharField(max_length=200)),
                ('Date_of_report', models.DateTimeField()),
            ],
        ),
    ]