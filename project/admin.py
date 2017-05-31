from django.contrib import admin
from .models import Project_Detail, Project_Image, Categorie



class Project_DetailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'order', 'date','type',)

 
class Project_ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'order',)
    list_filter = ('project',)
    
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('category',)
    
admin.site.register(Project_Detail, Project_DetailAdmin)
admin.site.register(Project_Image, Project_ImageAdmin)
admin.site.register(Categorie, CategorieAdmin)