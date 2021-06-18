from django.shortcuts import render

def get_page(request):
  return render(request, "page.html")