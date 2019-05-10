from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class PipelineForm(forms.Form):
    """TODO: ..."""

    # Form fields
    favorite_color = forms.CharField(
        label="What is your favorite color?",
        max_length=80,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(PipelineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "pipeline_form"
        self.helper.form_class = "pipeline"
        self.helper.form_method = "post"
        self.helper.form_action = "pipeline:submit"

        self.helper.add_input(Submit('submit', 'Submit'))
