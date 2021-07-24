# Generated by Django 3.2.5 on 2021-07-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ["-updated", "-created"]},
        ),
        migrations.RemoveField(
            model_name="book",
            name="deleted",
        ),
        migrations.AlterField(
            model_name="book",
            name="created",
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="updated",
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]