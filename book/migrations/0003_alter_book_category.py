# Generated by Django 3.2.5 on 2021-07-30 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="book.category"
            ),
        ),
    ]
