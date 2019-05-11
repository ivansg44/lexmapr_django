from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from lexmapr.pipeline.forms import PipelineForm


def get_pipeline_input(request):
    """Render input form for pipeline."""
    return render(request, "pages/pipeline.html", {"form": PipelineForm()})


@require_POST
def process_pipeline_input(request):
    """Processes data submitted to input form for pipeline."""

    # Create PipelineForm instance, with submitted data
    form = PipelineForm(request.POST, request.FILES)

    if form.is_valid():
        input_file = form.cleaned_data["input_file"]
        config_file = form.cleaned_data["config_file"]
        output_format = form.cleaned_data["output_format"]

    return redirect("pipeline:")
