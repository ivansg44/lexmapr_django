from datetime import datetime, timedelta

from django.db.models import (
    Model, CharField, BooleanField, TextField, DateTimeField
)
from django.urls import reverse


def get_expiry_date():
    return datetime.now() + timedelta(days=7)


class PipelineJob(Model):
    id = CharField(max_length=128, primary_key=True)
    complete = BooleanField()
    input = TextField()
    output = TextField()
    expires = DateTimeField(default=get_expiry_date)

    def get_absolute_url(self):
        return reverse('pipeline:temp', kwargs={"job_id": self.id})
