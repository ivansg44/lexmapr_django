from django.urls import path

from lexmapr_django.pipeline.views import (
    get_pipeline_input,
    process_pipeline_input
)

app_name = "pipeline"
urlpatterns = [
    path("", view=get_pipeline_input, name=""),
    path("submit", view=process_pipeline_input, name="submit")
]
