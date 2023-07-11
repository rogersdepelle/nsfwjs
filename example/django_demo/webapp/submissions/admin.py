from django.contrib import admin


from submissions.models import SubmissionResult, SubmissionResultByClass

admin.site.register(SubmissionResult)
admin.site.register(SubmissionResultByClass)
