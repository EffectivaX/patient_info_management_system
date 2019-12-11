from django import forms

class ProgressUpdateForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())

    def __init__(self, *args, **kwargs):
        super(ProgressUpdateForm, self).__init__(*args, **kwargs)
