# Generated by Django 3.2.7 on 2021-10-07 12:09

import django.core.validators
import django_inet.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0077_ix_add_sales_phone_email_949"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internetexchange",
            name="ixf_import_request_status",
            field=models.CharField(
                choices=[
                    ("queued", "Queued"),
                    ("importing", "Importing"),
                    ("finished", "Finished"),
                    ("error", "Import failed"),
                ],
                default="queued",
                help_text="The current status of the manual IX-F import request",
                max_length=32,
                verbose_name="Manual IX-F import status",
            ),
        ),
    ]
