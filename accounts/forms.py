from django.contrib.auth import get_user_model
from django.db.models import Q

from django import forms

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Andile',
    }))

    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'andilembele@cybertech.co.zw'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password'
    }))
    password2 =  forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password'
    }))

    # remember = forms.BooleanField(label='Remember Me',required=False, widget=forms.CheckboxInput(attrs={
    #     'class' : 'form-check-input'
    # }))


    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords Do not match')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Andile_Jaden'
    }))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password'
    }))

    # remember = forms.BooleanField(label='Remember Me',required=False, widget=forms.CheckboxInput(attrs={
        # 'class' : 'form-check-input'
    # }))

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
                Q(username__iexact=query) |
                Q(email__iexact=query)
            ).distinct()
        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError('Invaid credentials - user does not exist')
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError('Credentials are not correct')
        self.cleaned_data['user_obj'] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)
