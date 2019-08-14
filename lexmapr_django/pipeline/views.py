from random import getrandbits

from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from lexmapr_django.pipeline.forms import PipelineForm
from lexmapr_django.pipeline.utils import create_pipeline_job


def render_pipeline_form(request):
    """Render pipeline input form.

    If the user just submitted a form, also renders a hyperlink to the
    eventual results of their job.
    """
    job_id = None
    job_not_created = None

    # Just tried to create a job through ``process_pipeline_input``
    if "job_submission" in request.session:
        if request.session["job_submission"]["status"] == 200:
            job_id = request.session["job_submission"]["id"]
        # Something went wrong with form validation
        else:
            job_not_created = True

        request.session.pop("job_submission", None)
        request.session.modified = True

    return render(request, "pages/pipeline.html", {
        "form": PipelineForm(),
        "job_id": job_id,
        "job_not_created": job_not_created
    })


@require_POST
def process_pipeline_input(request):
    """Submits data from pipeline form submission to pipeline job."""
    form = PipelineForm(request.POST, request.FILES)
    request.session["job_submission"] = {}

    if form.is_valid():
        job_id = getrandbits(128)
        create_pipeline_job(job_id)

        request.session["job_submission"] = {"status": 200, "id": job_id}
    else:
        request.session["job_submission"] = {"status": 400, "id": None}

    return redirect("pipeline:")


def render_pipeline_results(request, job_id):
    """TODO:..."""
    return render(request, "pages/pipeline_results.html")
