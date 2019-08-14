from argparse import Namespace
from random import getrandbits
from tempfile import TemporaryDirectory

from lexmapr.pipeline import run

from lexmapr_django.pipeline.models import PipelineJob


def create_pipeline_job():
    """TODO:..."""
    job_id = getrandbits(128)
    pipeline_job = PipelineJob(id=job_id, complete=False, input="test",
                               output="test")
    pipeline_job.save()
    return job_id


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


def results_to_matrix(results):
    """Convert results to matrix for easy table rendering."""
    table = []

    results_rows = results.split("\n")
    for results_row in results_rows:
        table.append(results_row.split("\t"))

    # Remove row corresponding to empty row at end of results
    table.pop()

    return table
