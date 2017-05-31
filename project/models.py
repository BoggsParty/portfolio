from django.db import models
from django.utils.translation import gettext_lazy as _

class Project_Detail(models.Model):
    title = models.CharField(max_length=200, default='')
    category = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    DESIGN = 'D'
    BUILT = 'B'
    TYPE_CHOICES = (
        (DESIGN, 'Design'),
        (BUILT, 'Built'),
    )
    
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=DESIGN,
    )
    slug = models.SlugField(default='', help_text="Creates unique URL")
    description = models.TextField(default='')
    date = models.CharField(max_length=200, default='', help_text="Free text date description")
    duration = models.CharField(max_length=200, default='', help_text="Length of project")
    order = models.PositiveIntegerField(default=500, help_text="Order displayed.")
    #main_image = models.ForeignKey('Project_Image', on_delete=models.CASCADE, null=True)
    hidden = models.BooleanField(default=True, help_text="Ignore this, I don't know why it's here") 
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Detail")
        verbose_name_plural = _("Details")
        
    order.admin_order_field = 'order'
    
class Project_Image(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='', blank=True)
    project = models.ForeignKey('Project_Detail', on_delete=models.CASCADE, blank=True, null=True)
    order = models.PositiveIntegerField(default=500, help_text="Order displayed. 1 is main image")
    design_main = models.BooleanField(default=False)
    built_main = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = ('project', 'order',)
        verbose_name = _("Project Image")
        verbose_name_plural = _("Project Images")
        
class Categorie(models.Model):
    category = models.CharField(max_length=100, default='')
      
    def __str__(self):
        return self.category
        
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    