from django.shortcuts import render

# Create your views here.

def calcform(request):
    return render(request, 'romnumui/calcform.html')