# Generated by Django 4.2.3 on 2023-07-11 18:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SubmissionResult",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("image", models.FileField(upload_to="submissions/%Y/%m/%d")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Submission result",
                "verbose_name_plural": "Submissions results",
            },
        ),
        migrations.CreateModel(
            name="SubmissionResultByClass",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("class_name", models.CharField(max_length=50)),
                ("probability", models.FloatField()),
                (
                    "submission",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="submissions.submissionresult"),
                ),
            ],
            options={
                "verbose_name": "Submission result by class",
                "verbose_name_plural": "Submissions results by class",
            },
        ),
    ]
