# Generated by Django 3.1.4 on 2020-12-23 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("requirement", "0005_auto_20201223_2052"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requirement",
            name="test_cases",
            field=models.ManyToManyField(blank=True, to="requirement.TestCase", verbose_name="Test cases"),
        ),
    ]
