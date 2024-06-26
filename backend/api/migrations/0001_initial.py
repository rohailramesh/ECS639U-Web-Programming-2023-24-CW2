# Generated by Django 4.2.5 on 2023-10-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demonstrator_Claims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=100)),
                ('hours_worked', models.FloatField()),
                ('claim_form_submitted', models.BooleanField()),
                ('demonstrated_date', models.DateTimeField()),
            ],
        ),
    ]
