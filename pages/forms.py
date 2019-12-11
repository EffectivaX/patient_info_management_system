from django import forms

class ProgressUpdateForm(forms.Form):
    request_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Email Address'
    }))

    def __init__(self, *args, **kwargs):
        super(ProgressUpdateForm, self).__init__(*args, **kwargs)
