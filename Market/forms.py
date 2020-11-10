import datetime
from Market.models import Car, Cars
from django.forms import Textarea, ModelForm, TextInput, DateInput, CheckboxInput, FileInput, NumberInput, \
    Select, ModelChoiceField


class CarForm(ModelForm):

    name = ModelChoiceField(queryset=Cars.objects.all(), empty_label="Brand", widget=Select(attrs={'class':'form-control'}))

    class Meta:
        model = Car
        fields = ["name", "base", "car_body", "mileage", "year", "engine_type", "engine_size", "transmission",
                  "drive_unit", "price", "is_new", "photo"]
        Car.updated = datetime.datetime
        Car.created = datetime.datetime
        Car.available = True

        widgets = {
            "name": Textarea(attrs={
                'class': "form-control"
            }),
            "base": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Model"
            }),
            "car_body": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Base"
            }),
            "mileage": NumberInput(attrs={
                'class': "form-control",
                "placeholder": "Mileage",
                "step": "10000"
            }),
            "year": DateInput(attrs={
                'class': "form-control",
                "placeholder": "Date of creating"
            }),
            "engine_type": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Engine"
            }),
            "engine_size": NumberInput(attrs={
                'class': "form-control",
                "placeholder": "Size of engine"
            }),
            "transmission": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Transmission"
            }),
            "drive_unit": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Drive unit"
            }),
            "price": NumberInput(attrs={
                'class': "form-control",
                "placeholder": "Price"
            }),
            "is_new": CheckboxInput(attrs={
                'class': "input-group-text",
                'type': 'checkbox',
                "placeholder": "New car",
                "style": "width:30px; height:30px; margin: 0px"
            }),
            "photo": FileInput(attrs={
                'class': "form-control",
                'type': "file",
                "style": "width: 100%",
            }),

        }