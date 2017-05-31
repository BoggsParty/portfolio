from django.contrib import admin
from .models import About, About_Images, Resume_Content, Resume_PDF

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','active',)
    
admin.site.register(About, AboutAdmin)

class About_ImagesAdmin(admin.ModelAdmin):
    list_display = ('title','active',)
    
admin.site.register(About_Images, About_ImagesAdmin)

class Resume_ContentAdmin(admin.ModelAdmin):
    list_display = ('title','active','order',)
    order_by = ('order',)
    
admin.site.register(Resume_Content, Resume_ContentAdmin)

class Resume_PDFAdmin(admin.ModelAdmin):
    list_display = ('version_title','date',)
    
admin.site.register(Resume_PDF, Resume_PDFAdmin)
