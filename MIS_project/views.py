# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse
# def reports (request):
# #     # return HttpResponse("Tracking")   
#   return render(request,'button.html')
# from django.template import loader

# def reports(request):
#  template =  loader.get_template('home.html')
#  return HttpResponse(template.render())   
 
from django.http import HttpResponse
from django.template import loader

def reports(request):
  template =loader.get_template('button.html')
  return HttpResponse(template.render())


def paragraph(request):
  template =loader.get_template('para.html')
  return HttpResponse(template.render())

def hover(request):
    template = loader.get_template('hover.html')
    return HttpResponse(template.render())

# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#   template = loader.get_template('button.html')
#   return HttpResponse(template.render())