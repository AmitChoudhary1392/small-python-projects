from django import forms

class LocationForm(forms.Form):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "City, Country etc.",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )