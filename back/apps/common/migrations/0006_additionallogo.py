# Generated by Django 3.1.4 on 2021-07-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_assessmentbutton'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='additional_logo')),
                ('enabled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Additional logo',
            },
        ),
    ]
