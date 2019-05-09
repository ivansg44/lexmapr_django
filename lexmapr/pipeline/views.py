from django.shortcuts import render

from lexmapr.pipeline.forms import PipelineForm


def get_pipeline_input(request):
    form = PipelineForm()
    return render(request, "pages/pipeline.html", {"form": form})
