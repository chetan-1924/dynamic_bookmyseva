from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about_us_page(request):
    return render(request, 'about.html')
def pricing(request):
    return render(request, 'pricing.html')
def contact(request):
    return render(request, 'contact.html')
def service(request):
    return render(request, 'service.html')
# def contact(request):
#     return render(request, 'contact.html')
