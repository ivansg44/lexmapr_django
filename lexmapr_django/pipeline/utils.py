from argparse import Namespace
from random import getrandbits
from tempfile import TemporaryDirectory

from django.core.files.base import ContentFile
from lexmapr.pipeline import run

from lexmapr_django.pipeline.models import PipelineJob


def create_pipeline_job(input_file):
    """TODO:..."""
    job_id = getrandbits(128)
    job = PipelineJob(id=job_id)
    job.save()

    job.input_file.save(str(job_id) + ".csv", input_file)
    job.output_file.save(str(job_id) + ".tsv", ContentFile(""))

    try:
        execute_pipeline_job(job)
    except Exception as e:
        job.err = True
        job.err_msg = str(e)
        job.save()

    return job_id


def execute_pipeline_job(job):
    """TODO:..."""
    run(Namespace(input_file=job.input_file.path,
                  config="envo_foodon_config.json", format="basic",
                  output=job.output_file.path, version=False, bucket=True))

    job.complete = True
    job.save()


def run_lexmapr(input_file):
    """TODO:..."""

    # Need to convert InMemoryUploadedFile values to actual files
    with TemporaryDirectory() as tmp_dir:
        tmp_input_path = tmp_dir + "/" + str(input_file)
        tmp_output_path = tmp_dir + "/output.tsv"

        with open(tmp_input_path, "ab") as tmp_input_fp:
            for input_file_chunk in input_file.chunks():
                tmp_input_fp.write(input_file_chunk)
        try:
            run(Namespace(input_file=tmp_input_path,
                          config="envo_foodon_config.json",
                          format="basic", output=tmp_output_path,
                          version=False, bucket=True))
        except Exception as e:
            return "Oops! Something went wrong"

        with open(tmp_output_path, "r") as tmp_output_fp:
            ret = tmp_output_fp.read()

    return ret


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
