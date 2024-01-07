from django.shortcuts import render
from .models import UploadedImage
from .forms import UploadImageForm

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Retrieve the newly uploaded image
            latest_image = UploadedImage.objects.latest('uploaded_at')
            return render(request, 'upload_image.html', {'form': form, 'image': latest_image})
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})
