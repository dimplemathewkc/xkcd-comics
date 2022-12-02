# Generated by Django 4.1.3 on 2022-12-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comic",
            name="day",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="comic",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comic",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comic",
            name="issue",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comic",
            name="month",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="comic",
            name="year",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
