from django.shortcuts import get_object_or_404, render, redirect
from .models import Project_Detail, Categorie, Project_Image
from django.db.models import F

def projects(request):
    built_image = Project_Image.objects.filter(built_main=True).latest('id')
    design_image = Project_Image.objects.filter(design_main=True).latest('id')
    return render(request, 'project/project-main.html', {'built_image':built_image,'design_image':design_image,})
    
def design(request):
    project = Project_Detail.objects.filter(type = "D").order_by('order').exclude(hidden=True)
    #image = Project_Image.objects.filter(order="1").filter(type = "D")
    project_count = project.count()
    return render(request, 'project/design.html', {'project':project,'project_count':project_count,})
    
def built(request):
    project = Project_Detail.objects.filter(type = "B").order_by('order').exclude(hidden=True)
    #image = Project_Image.objects.filter(order="1").filter(type = "D")
    project_count = project.count()
    return render(request, 'project/built.html', {'project':project,'project_count':project_count,})

def project_main(request, slug):
    project = get_object_or_404(Project_Detail, slug=slug)
    main_image = Project_Image.objects.filter(project=project).get(order="1")
    odd_images = Project_Image.objects.annotate(odd=F('order') % 2).filter(odd=True).filter(project=project).order_by('order')
    even_images = Project_Image.objects.annotate(odd=F('order') % 2).filter(odd=False).filter(project=project).order_by('order')
    image_count = odd_images.count() + even_images.count() 
    slug = slug
    return render(request, 'project/project-detail-main.html', {'project':project,'main_image':main_image,'even_images':even_images,'odd_images':odd_images,'slug':slug,})  


def project_detail(request, slug, order):
    project = get_object_or_404(Project_Detail, slug=slug)
    main_image = Project_Image.objects.filter(project=project).get(order=order)
    odd_images = Project_Image.objects.annotate(odd=F('order') % 2).filter(odd=True).filter(project=project)
    even_images = Project_Image.objects.annotate(odd=F('order') % 2).filter(odd=False).filter(project=project)
    image_count = odd_images.count() + even_images.count() 
    slug = slug
    backward = main_image.order-1
    forward = main_image.order+1
    if main_image.order == image_count:
        forward = 1
    else:
        pass
    if order == '1':
        return render(request, 'project/project-detail-1.html', {'project':project,'main_image':main_image,'even_images':even_images,'odd_images':odd_images,'forward':forward,'slug':slug,})
    else:    
        return render(request, 'project/project-detail-rest.html', {'project':project,'main_image':main_image,'even_images':even_images,'odd_images':odd_images,'forward':forward,'backward':backward,'slug':slug,})
