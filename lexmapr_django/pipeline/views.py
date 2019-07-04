from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from lexmapr_django.pipeline.forms import PipelineForm
from lexmapr_django.pipeline.utils import results_to_matrix, run_lexmapr


def render_pipeline_form(request):
    """Render input form for pipeline."""

    # Just successfully ran ``process_pipeline_input``
    if "results" in request.session:
        results = request.session["results"]
        # Remove results from session
        request.session.pop("results", None)
        request.session.modified = True
    else:
        results = ""

    return render(request, "pages/pipeline.html", {"form": PipelineForm(),
                                                   "results": results})


@require_POST
def process_pipeline_input(request):
    """Processes data submitted to input form for pipeline."""

    # Create PipelineForm instance, with submitted data
    form = PipelineForm(request.POST, request.FILES)

    if form.is_valid():
        input_file = form.cleaned_data["input_file"]

        results = run_lexmapr(input_file)
    else:
        results = "Form not valid"

    request.session["results"] = results_to_matrix(results)
    return redirect("pipeline:")
