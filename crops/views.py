# crops/views.py
from django.shortcuts import render, get_object_or_404
from .models import CropProfile


# this view shows all 20 crops in a grid, like a directory page
# also handles the search bar from the homepage (crop_name in the url)
def crop_list(request):
    crops = CropProfile.objects.all().order_by('crop_name')

    # if someone searched for a crop name from the homepage search bar
    # this filters the list down to matching crops only
    search_query = request.GET.get('crop_name')
    if search_query:
        crops = crops.filter(crop_name__icontains=search_query) # icontains - means case-insensitive contains ; basically find anything that has this text inside it

    context = {
        'crops': crops,
        'search_query': search_query,
    }
    return render(request, 'crops/crop_list.html', context)


# this view shows full details for one single crop
def crop_detail(request, crop_name): # crop_name comes from the url : for eg crops/rice/ ...
    crop = get_object_or_404(CropProfile, crop_name__iexact=crop_name) # iexact - means case insensitive exact match; basically find the one exact match

    context = {
        'crop': crop,
    }
    return render(request, 'crops/crop_detail.html', context)
