# devices/forms.py
from django import forms
from .models import Device

# -------------- Form To add a new Device --------------
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device_name'].widget.attrs.update({
            'placeholder': 'e.g. Backyard Field Sensor', # Act as a placeholder for that 'Device Name' field
        })
