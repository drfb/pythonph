from django.conf import settings
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from common.utils import notify_slack
from .models import Company, Job


class JobAdmin(MarkdownxModelAdmin):
    def save_model(self, request, obj, form, change):
        data = form.cleaned_data
        super().save_model(request, obj, form, change)

        if 'is_approved' in form.changed_data and data.get('is_approved'):
            notify_slack(
                '✨ *New job posting* ✨ \n {} \n {} \n\n :python: <https://python.ph/jobs|python.ph/jobs>'.format(obj.title, obj.company.name),
                settings.SLACK_JOBS_CHANNEL
            )


admin.site.register(Company, MarkdownxModelAdmin)
admin.site.register(Job, JobAdmin)
