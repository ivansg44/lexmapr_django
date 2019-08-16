from argparse import Namespace

from lexmapr.pipeline import run

from config import celery_app
from lexmapr_django.pipeline.models import PipelineJob


@celery_app.task()
def run_lexmapr(job_id):
    """TODO:..."""
    job = PipelineJob.objects.get(id=job_id)
    try:
        run(Namespace(input_file=job.input_file.path,
                      config="envo_foodon_config.json", format="basic",
                      output=job.output_file.path, version=False, bucket=True))
    except Exception as e:
        job.err = True
        job.err_msg = str(e)

    job.complete = True
    job.save()
