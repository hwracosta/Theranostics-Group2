from .models import *
from django import forms
from .widgets import MultipleFileInput  # Use your custom widget here.

class AddPostTherapy(forms.ModelForm):
    lesion_images = forms.FileField(
        widget=MultipleFileInput(),
        required=False
    )
    dosimetry_images = forms.FileField(
        widget=MultipleFileInput(),
        required=False
    )

    class Meta:
        model = PostTherapy
        fields = [
            'date_of_post_therapy',
            'post_therapy_scan_hours',
            'with_spect_ct',
            'lesions',
            'bone_lesion_details',
            'salivary_gland',
            'kidney_left',
            'kidney_right',
        ]
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)',
        }

    def clean_lesion_images(self):
        return self._validate_file_types(self.cleaned_data.get('lesion_images'))

    def clean_dosimetry_images(self):
        return self._validate_file_types(self.cleaned_data.get('dosimetry_images'))

    def _validate_file_types(self, files):
        allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf']
        if files:
            for f in files:
                if f.content_type not in allowed_types:
                    raise forms.ValidationError(
                        f"{f.name} is not a valid file type. Allowed types: PNG, JPG, GIF, PDF."
                    )
        return files

class EditPostTherapy(AddPostTherapy):
    """This inherits from AddPostTherapy if the fields remain the same."""
    pass