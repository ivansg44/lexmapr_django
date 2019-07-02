from django.urls import path

from lexmapr_django.pipeline.views import (
    render_pipeline_form,
    process_pipeline_input
)

app_name = "pipeline"
urlpatterns = [
    path("", view=render_pipeline_form, name=""),
    path("submit", view=process_pipeline_input, name="submit")
]
