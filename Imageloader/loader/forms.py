from django import forms
from django.core import validators


class UploadImageForm (forms.Form):
    file = forms.ImageField(validators=[validators.FileExtensionValidator(allowed_extensions=('gif', 'jpg', 'png'))],
                            error_messages={'invalid extension': 'Этот формат не поддерживается'})


