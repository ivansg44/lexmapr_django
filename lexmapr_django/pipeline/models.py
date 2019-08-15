from datetime import datetime, timedelta

from django.contrib.postgres.fields import ArrayField
from django.db.models import (
    Model, BooleanField, CharField, DateTimeField, FileField, TextField
)
from django.urls import reverse


def get_expiry_date():
    return datetime.now() + timedelta(days=7)


class PipelineJob(Model):
    id = CharField(max_length=128, primary_key=True)
    complete = BooleanField(default=False)
    input_file = FileField(upload_to="input_files/", blank=True)
    output_file = FileField(upload_to="output_files/", blank=True)
    expires = DateTimeField(default=get_expiry_date)
    err = BooleanField(default=False)
    err_msg = TextField(blank=True)

    def get_absolute_url(self):
        return reverse('pipeline:temp', kwargs={"job_id": self.id})
