from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about_us_page(request):
    return render(request, 'about.html')
# def contact(request):
#     return render(request, 'contact.html')
