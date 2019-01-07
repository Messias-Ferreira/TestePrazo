from django import forms

class Anexa_arquivo(forms.Form):
    pdf = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
        'class':'custom-file-input',
        'id':'input_arquivo',
        'type':'file'
    }),
    )