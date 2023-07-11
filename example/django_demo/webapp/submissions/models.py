import os
import uuid

import requests

from django.db import models
from django.urls import reverse


class SubmissionResult(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    image = models.FileField(upload_to="submissions/%Y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Submission result"
        verbose_name_plural = "Submissions results"

    def __str__(self):
        return f"{self.created_at}"

    def get_absolute_url(self):
        return reverse("submission-result-detail", kwargs={"pk": self.pk})

    def check_content(self):
        NSFW_API = os.environ.get("NSFW_API", "http://nsfwjsapi:8080/nsfw")
        results = requests.post(NSFW_API, files={"image": self.image.file}).json()
        for result in results:
            SubmissionResultByClass.objects.create(
                submission=self,
                class_name=result["className"],
                probability=result["probability"],
            )

    def save(self, *args, **kwargs):
        super(SubmissionResult, self).save(*args, **kwargs)
        self.check_content()


class SubmissionResultByClass(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    submission = models.ForeignKey("submissions.SubmissionResult", on_delete=models.PROTECT, related_name="results")
    class_name = models.CharField(max_length=50)
    probability = models.FloatField()

    class Meta:
        verbose_name = "Submission result by class"
        verbose_name_plural = "Submissions results by class"
        ordering = ["-probability"]

    def __str__(self):
        return f"{self.submission} - {self.class_name}"
