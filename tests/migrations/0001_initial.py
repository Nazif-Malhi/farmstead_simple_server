# Generated by Django 4.1.4 on 2023-05-07 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("test_name", models.CharField(max_length=25)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "farmer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SimpleCropRecomendation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("soil_type", models.CharField(max_length=25)),
                ("temprature", models.CharField(max_length=25)),
                ("humidity", models.CharField(max_length=25)),
                ("ph", models.CharField(max_length=25)),
                ("rain", models.CharField(max_length=25)),
                ("result", models.CharField(max_length=25)),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tests.test"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PestDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pest_image", models.ImageField(upload_to="pest_detection")),
                ("result", models.CharField(max_length=25)),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tests.test"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FertilizerRecomendation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("temprature", models.CharField(max_length=25)),
                ("humidity", models.CharField(max_length=25)),
                ("moisture", models.CharField(max_length=25)),
                ("soil_type", models.CharField(max_length=25)),
                ("crop_type", models.CharField(max_length=25)),
                ("nitrogen_val", models.CharField(max_length=25)),
                ("phosphorus_val", models.CharField(max_length=25)),
                ("potassium_val", models.CharField(max_length=25)),
                ("result", models.CharField(max_length=25)),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tests.test"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CropDiseaseDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "crop_desease_image",
                    models.ImageField(upload_to="crop_desease_detection"),
                ),
                ("result", models.CharField(max_length=25)),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tests.test"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdvanceCropRecomendation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nitrogen_val", models.CharField(max_length=25)),
                ("phosphorus_val", models.CharField(max_length=25)),
                ("potassium_val", models.CharField(max_length=25)),
                ("soil_type", models.CharField(max_length=25)),
                ("temprature", models.CharField(max_length=25)),
                ("humidity", models.CharField(max_length=25)),
                ("ph", models.CharField(max_length=25)),
                ("rain", models.CharField(max_length=25)),
                ("result", models.CharField(max_length=25)),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tests.test"
                    ),
                ),
            ],
        ),
    ]
