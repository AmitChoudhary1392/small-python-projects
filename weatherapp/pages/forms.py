from django import forms

class LocationForm(forms.Form):
    location = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "City",
                # "class": "textarea is-success is-medium",
            }
        ),
        label="Location",

    )
    

