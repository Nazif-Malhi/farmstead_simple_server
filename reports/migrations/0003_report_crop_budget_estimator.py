# Generated by Django 4.1.4 on 2023-01-19 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cropbudgetestimator", "0001_initial"),
        ("reports", "0002_alter_report_test"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="crop_budget_estimator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cropbudgetestimator.cropbudget",
            ),
        ),
    ]