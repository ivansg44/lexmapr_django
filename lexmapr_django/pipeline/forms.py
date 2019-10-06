from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.validators import FileExtensionValidator


class PipelineForm(forms.Form):
    input_file = forms.FileField(
        label="Input file",
        validators=[FileExtensionValidator(["csv", "tsv"])]
    )

    def __init__(self, *args, **kwargs):
        super(PipelineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "pipeline_form"
        self.helper.form_class = "pipeline"
        self.helper.form_method = "post"
        self.helper.form_action = "pipeline:submit"

        self.helper.add_input(Submit('submit', 'Submit'))
