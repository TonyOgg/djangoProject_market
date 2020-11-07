from Market.models import Car
from django.forms import ModelForm, TextInput

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "base", "car_body", "mileage", "year", "engine_type", "engine_size", "transmission",
                  "drive_unit", "price", "is_new", "photo"]
        widgets = {
            "name": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Brand"
            })
        }