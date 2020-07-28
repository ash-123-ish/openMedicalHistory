# Generated by Django 3.0.5 on 2020-04-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=200)),
                ('Aadhar_number', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=200)),
                ('Age', models.IntegerField(default=0)),
                ('Sex', models.CharField(max_length=5)),
                ('Phone_number', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=200)),
                ('CR_no', models.IntegerField()),
                ('Prescription', models.ImageField(blank=True, max_length=255, null=True, upload_to='prescription/%Y/%m/%d/')),
                ('Prescription_text', models.CharField(max_length=2000)),
                ('Online_status', models.IntegerField(default=0)),
                ('Diagnosis', models.CharField(max_length=200)),
                ('Status', models.CharField(max_length=200)),
                ('Doctor_name', models.CharField(max_length=200)),
                ('Doctor_dept', models.CharField(max_length=200)),
                ('Date_of_meeting', models.DateTimeField()),
            ],
        ),
    ]