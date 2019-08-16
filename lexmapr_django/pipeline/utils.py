from random import getrandbits

from django.core.files.base import ContentFile

from lexmapr_django.pipeline.models import PipelineJob
from lexmapr_django.pipeline.tasks import run_lexmapr


def create_pipeline_job(input_file):
    """TODO:..."""
    job_id = getrandbits(128)
    job = PipelineJob(id=job_id)
    job.save()

    job.input_file.save(str(job_id) + ".csv", input_file)
    job.output_file.save(str(job_id) + ".tsv", ContentFile(""))

    run_lexmapr.delay(job_id)

    return job_id


def results_to_matrix(job):
    """TODO:..."""
    table = []

    results = job.output_file.read().decode("utf-8")
    results_rows = results.split("\n")
    for results_row in results_rows:
        table.append(results_row.split("\t"))

    # Remove row corresponding to empty row at end of results
    table.pop()

    return table
