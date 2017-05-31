from django.db import models
from django.utils.translation import gettext_lazy as _

class About(models.Model):
    title = models.CharField(default='', max_length=200)
    content = models.TextField(default='', blank=True)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("About")
        
class About_Images(models.Model):
    title = models.CharField(default='', max_length=200, help_text = "internal title")
    image = models.ImageField(blank=True)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        
class Resume_Content(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    active = models.BooleanField(default = False)
    order = models.PositiveSmallIntegerField(default = 1, help_text="Use this to order the sections")
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = _("Resume Content")
        verbose_name_plural = _("Resume Content")
        
class Resume_PDF(models.Model):
    version_title = models.CharField(max_length=200, default='')
    file = models.FileField(upload_to='resume/%y/%m/%d/', help_text="Uses most recent")
    date = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.version_title
        
    class Meta:
        verbose_name = _("Resume PDF")
        verbose_name_plural = _("Resume PDF")