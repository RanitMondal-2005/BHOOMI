# devices/views.py
'''
CORE MECHANISM OF OUR UUID (API KEY):
1. Farmer registers through the website and adds a Device → Django creates a Device row, auto-generates a unique UUID, permanently tied via owner = models.ForeignKey(User, ...) to that farmer’s account.
2. That UUID gets embedded into the ESP32’s firmware (the manual step)
3. Every time that specific ESP32 sends data, it includes that UUID
4. Our view does Device.objects.get(api_key=api_key) in views.py of plant/soil monitor — this single lookup is what “synchronizes” the incoming anonymous HTTP request back to exactly one physical device, owned by exactly one farmer, every time, with zero ambiguity.
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Device
from .forms import DeviceForm


# ----------- Shows all devices belonging to the logged in farmer -----------
@login_required
def device_list(request):
    devices = Device.objects.filter(owner=request.user)
    return render(request, 'devices/device_list.html', {'devices': devices})


# ----------- Handles adding a new device ----------------------
@login_required
def add_device(request):

    # a farmer can add max 3 devices, not unlimited
    existing_count = Device.objects.filter(owner=request.user).count()
    if existing_count >= 3:
        messages.error(request, 'You can register a maximum of 3 devices per account.')
        return redirect('device_list')

    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False) # Dont Save the device first - first register the owner then save
            device.owner = request.user
            device.save()
            messages.success(request, 'Device added successfully.')
            return redirect('device_list')
    else:
        form = DeviceForm()

    return render(request, 'devices/add_device.html', {'form': form})


# ---------------------- removes a device ----------------------
# we check owner=request.user here so a farmer cannot delete someone elses device
# just by guessing the device id in the url
@login_required
def delete_device(request, device_id):
    device = get_object_or_404(Device, id=device_id, owner=request.user)
    device.delete()
    messages.success(request, 'Device removed.')
    return redirect('device_list')
