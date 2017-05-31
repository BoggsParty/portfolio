from django.shortcuts import render, render_to_response
from project.models import Project_Image
from .models import About, About_Images, Resume_Content, Resume_PDF
   
def home(request):
    images = Project_Image.objects.order_by('?')
    return render(request, 'main/home.html', {'images':images})

def about(request): 
    content = About.objects.filter(active=True)
    images = About_Images.objects.filter(active=True)
    return render(request, 'main/about.html', {'content':content,'images':images})
    
def contact(request):
    return render(request, 'main/contact.html')
    
def resume(request):
    content = Resume_Content.objects.filter(active=True).order_by('order')
    pdf = Resume_PDF.objects.latest('id')
    return render(request, 'main/resume.html', {'content':content,'pdf':pdf,})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response