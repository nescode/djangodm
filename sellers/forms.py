from django import forms

# New seller forms

class NewSellerForm(forms.Form):
    agree = forms.BooleanField(label='Agree to Terms', widget=forms.CheckboxInput)
