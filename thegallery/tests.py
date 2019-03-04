from django.test import TestCase
from .models import Location,categories,Image

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.pakistan= Location(location_name="Pakistan")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pakistan,Location))

       # Testing Save Method
    def test_save_method(self):
        self.pakistan.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)     

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nature= categories(category_name="Nature")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,categories))

    def test_save_method(self):
        self.nature.save_category()
        category = categories.objects.all()
        self.assertTrue(len(category) > 0)      

class ImagesTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location1 = Location(location_name="pakistan")
        self.category1 = categories(category_name = "wild")
        self.category2 = categories(category_name = "nature")
        self.newImg= Image(name = 'waterfall', description ='taken at karura forest', img ="/waterfall.jpeg",location=self.location1)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.newImg,Image))
       
      # Testing Save Method
    def test_save_method(self):
        self.location1.save_location()
        self.newImg.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)    


    #       name = models.CharField(max_length=50)
    # description = models.TextField()
    # img= models.ImageField(height_field=None, width_field=None, max_length=None)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # categories = models.ManyToManyField(categories)
