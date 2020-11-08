import datetime
from Market.models import Car, Cars
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput, FileInput, NumberInput, ModelChoiceField


class CarForm(ModelForm):

    name = ModelChoiceField(queryset=Cars.objects.values_list("name", flat=True), empty_label="Brand")

    class Meta:
        model = Car
        fields = ["base", "car_body", "mileage", "year", "engine_type", "engine_size", "transmission",
                  "drive_unit", "price", "is_new", "photo"]
        Car.updated = datetime.datetime
        Car.created = datetime.datetime
        Car.available = True

        widgets = {
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
                "placeholder": "Mileage"
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
                "placeholder": "New car"
            }),
            "photo": FileInput(attrs={
                'class': "form-control",
                'type': "file",
                "placeholder": "Photo"
            }),

        }