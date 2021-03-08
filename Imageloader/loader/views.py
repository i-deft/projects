from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
from .models import UploadImage
from rest_framework.response import Response
from .serializers import UploadImageSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.views import APIView


def index(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            for f in request.FILES.getlist('file'):
                img = UploadImage(file=form.cleaned_data['file'])
                img.save()

            return HttpResponse('')
    else:
        form = UploadImageForm()
        context = {'form': form}
        return render(request, 'loader/index.html', context)


class UploadImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        images = UploadImage.objects.all()
        serializer = UploadImageSerializer(images, many=True)
        return Response({"UploadImages": serializer.data})

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = UploadImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




