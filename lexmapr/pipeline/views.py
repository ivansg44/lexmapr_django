from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from lexmapr.pipeline.forms import PipelineForm


def get_pipeline_input(request):
    """Render input form for pipeline."""
    return render(request, "pages/pipeline.html", {"form": PipelineForm()})


@require_POST
def process_pipeline_input(request):
    """Processes data submitted to input form for pipeline."""

    # Create PipelineForm instance, with data from POST request
    form = PipelineForm(request.POST)

    # Input accessible through `form.data`

    return redirect("pipeline:")
