from django.db import models
#from django.template.defaultfilters import slugify

class Material(models.Model):
    name = models.CharField(max_length=128,unique=True,blank=False)
    units = models.CharField(max_length=30,blank=False)
    data_source = [ models.TextField(),
                    models.URLField(),
                  ]
    description = models.TextField();

    #def save(self, *args, **kwargs):
        #self.slug = slugify(self.name)
        #super(Category,self).save(*args, **kwargs)

    #Define what is printed when the object is returned
    def __unicode__(self):
        return self.name
