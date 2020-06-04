from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FileRequest, ImageResponse
from .forms import RequestForm
from .modules import visualizing


# 뷰 : 모델을 사용하여 템플릿을 제공 (뷰에서 하드코딩을 한다면 디자인도 가능하겠지만, 템플릿을 통해 분리하는 것이 바람직)


def fileRequest(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imageResponse')
    form = RequestForm()
    context = {
        'form':form
    }
    return render(request, 'app01/fileRequestTemplate.html', context)


def imageResponse(request):
    visualizing()
    image = ImageResponse.objects.all().order_by('-time')[0]
    print(image.title)
    print(image.imagePath)
    print(image.getImagePath())
    context = {
        'image': image
    }
    return render(request, 'app01/imageResponseTemplate.html', context)
