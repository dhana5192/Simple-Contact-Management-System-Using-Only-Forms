from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        label='Name'
    )
    mobile_no = forms.CharField(
        required=True,
        label='Mobile Number'
    )
    alt_mobile_no = forms.CharField(
        required=False,
        label='Alternate Mobile Number(optional)'
    )
    email = forms.EmailField(
        required=False,
        label='Email(optional)'
    )