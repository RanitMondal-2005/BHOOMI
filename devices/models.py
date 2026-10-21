# devices/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid # Python function used to generate a Universally Unique Identifier (UUID). It generates a random 128-bit number (represented as a 32-character hexadecimal string)


# this model represents one physical esp32 device belonging to a farmer
# the esp32 will send its api_key with every request, so our backend
# knows which farmer and which device the incoming sensor data belongs to
class Device(models.Model):

    # this lets a device be in only one of these states at a time
    # this is what enforces the "only one feature active at once" rule
    MODE_CHOICES = [
        ('idle', 'Idle'),
        ('soil_analyzing', 'Soil Analyzing'),
        ('plant_monitoring', 'Plant Monitoring'),
    ]
    
    # Connect the Owner (User) for this particular device registered
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')

    # a simple name so the farmer can tell devices apart if they have more than one
    device_name = models.CharField(max_length=100, default='My BHOOMI Device')

    # this is the secret key the esp32 sends with every request
    # uuid4 generates a long random value automatically
    api_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    current_mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='idle')

    # this stores when the device last sent any data at all
    last_seen = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_name} ({self.owner.username})"
