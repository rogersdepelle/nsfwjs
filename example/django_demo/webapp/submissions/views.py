from django.views.generic import CreateView, DetailView

from submissions.models import SubmissionResult


class SubmissionResultCreateView(CreateView):
    model = SubmissionResult
    fields = ["image"]


class SubmissionResultDetailView(DetailView):
    model = SubmissionResult
