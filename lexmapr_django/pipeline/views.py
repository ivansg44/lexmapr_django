from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from lexmapr_django.pipeline.forms import PipelineForm
from lexmapr_django.pipeline.utils import run_lexmapr


def render_pipeline_form(request):
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
        full_format = form.cleaned_data["full_format"]

        results = run_lexmapr(input_file, config_file, full_format)

    return redirect("pipeline:")
