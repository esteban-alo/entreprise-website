from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your name'
        }), min_length=3, max_length=100)
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your email'
        }))
    content = forms.CharField(label="Message", required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Write a message'
        }), min_length=20, max_length=100)
