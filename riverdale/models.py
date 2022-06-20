from django.db import models
from django.contrib.auth.models import User




# Create your models here
class Neighborhood(models.Model):
    title=models.CharField(null=True,max_length=200)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    location=models.CharField(null=True,max_length=200)
    occupants_count=models.CharField(null=True,max_length=200)
    bio=models.TextField(null=True,max_length=1000)
    testimonials1=models.CharField(null=True,max_length=1000)
    testimonials2=models.CharField(null=True,max_length=1000)
    testimonials3=models.CharField(null=True,max_length=1000)

    @classmethod
    def neighborhood_id(cls,id):
        # id = Neighborhood.all()
        t = cls.objects.filter(pk = id)
        return t

    def save_neighborhood(self):
        self.save()
    
    def update_neighborhood(self):
        self.update()

    def delete_neighborhood(self): 
        self.delete()

    @classmethod
    def update_neighborhood(cls,current_neighborhood,new_neighborhood):
        updated_neighborhood = Neighborhood.objects.filter(neighborhood_name=current_neighborhood).update(name=new_neighborhood)
        return updated_neighborhood

    # search
    @classmethod
    def search_by_title(cls,searched_term):
        neighborhood = cls.objects.filter(title__icontains=searched_term)
        return neighborhood



    def __str__(self):
        return(self.title)

class User(models.Model):
    name=models.CharField(null=True,max_length=200)
    house_no=models.CharField(null=True,max_length=3)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    neighborhood_id=models.OneToOneField(Neighborhood,related_name='neighborhoods',on_delete=models.CASCADE,null=True, blank=True)
    email_address=models.EmailField(null=True,max_length=200)
    contacts=models.CharField(null=True,max_length=200)
    user = models.OneToOneField(User, related_name='user_prf',on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return(self.name)
        
class Business(models.Model):
    b_name=models.CharField(null=True,max_length=200)
    contacts=models.CharField(null=True,max_length=200)
    email=models.EmailField(null=True,max_length=200)
    user=models.ForeignKey(User,related_name='user_bsn',on_delete=models.CASCADE,null=True, blank=True)
    neighborhood_id=models.ForeignKey(Neighborhood,related_name='neighborhood_id',on_delete=models.CASCADE,null=True, blank=True)
    
    @classmethod
    def business_id(cls,id):
        # id = Neighborhood.all()
        t = cls.objects.filter(pk = id)
        return t

    def save_business(self):
        self.save()
    
    def update_business(self):
        self.update()

    def delete_business(self): 
        self.delete()

    @classmethod
    def update_business(cls,current_business,new_business):
        updated_business = Business.objects.filter(business_name=current_business).update(name=new_business)
        return updated_business
    
    def __str__(self):
        return(self.b_name)

class Images(models.Model):
    neighborhood=models.ForeignKey(Neighborhood,related_name='neighborhood_img',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image')
    id=models.IntegerField(primary_key=True)
    name = models.CharField(null=True,max_length=10)


    def __str__(self):
        return(self.name)



class Post(models.Model):
    name = models.CharField(null=True,max_length=50)
    caption = models.TextField(null=True,max_length=50)
    id=models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    images = models.ImageField(default='default.jpg', upload_to='photo_images')
    created=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,related_name='user_post',on_delete=models.CASCADE,null=True, blank=True)
    neighborhood_id=models.ForeignKey(Neighborhood,related_name='neighborhood_post',on_delete=models.CASCADE,null=True, blank=True)
    def save_post(self):
        self.save()
    
    def delete_post(self): 
        self.delete()

    @classmethod
    def update_image(cls,current_img,new_img):
        updated_img = Post.objects.filter(image_name=current_img).update(name=new_img)
        return updated_img


    def __str__(self):
        return (self.name)
