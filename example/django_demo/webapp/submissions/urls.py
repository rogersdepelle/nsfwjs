from django.urls import path

from submissions import views


urlpatterns = [
    path("", views.SubmissionResultCreateView.as_view(), name="submission-result-create"),
    path("submissions/<uuid:pk>", views.SubmissionResultDetailView.as_view(), name="submission-result-detail"),
]
