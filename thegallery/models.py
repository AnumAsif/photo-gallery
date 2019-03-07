from django.db import models

class categories(models.Model):

    category_name = models.CharField(max_length = 60)
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(self,id,category_name):
        self.objects.filter(id = id).update(category_name= category_name) 
    @classmethod
    def get_categories(cls):
        img_categories = cls.objects.all()    
        return img_categories 

class Location(models.Model):
    location_name = models.CharField(max_length = 60)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,location_name):
        cls.objects.filter(id = id).update(location_name = location_name)

    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    img= models.ImageField(height_field=None, width_field=None, max_length=None)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    categories = models.ManyToManyField(categories)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, description):
        cls.objects.filter(id=id).update(description = description)

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def get_image_by_category(cls, categoryname):
        image = cls.objects.filter(categories__category_name__icontains=categoryname)    
        return image

    @classmethod
    def search_image(cls,categoryId):
        images = cls.objects.filter(categories__id= categoryId)
        return images

    @classmethod
    def search_image_by_location(cls,location):
        images = cls.objects.filter(location= location)
        return images
      


