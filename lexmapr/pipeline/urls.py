from django.urls import path

from lexmapr.pipeline.views import get_pipeline_input

app_name = "pipeline"
urlpatterns = [
    path("", view=get_pipeline_input, name="")
]
