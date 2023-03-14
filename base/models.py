from django.db import models
from django.contrib.auth.models import User

# Models
    
# the type of the rental
class Category(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
    
# the information of a rental
class Rental(models.Model):
    post_title = models.CharField(max_length=90)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200)
    amenities = models.CharField(max_length=250)
    rent = models.IntegerField()
    availability = models.DateField()
    unit_iamge = models.ImageField(null=True, blank=True, upload_to='images/')
    
    date_posted = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    
    # applies referential integrity constraints
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-time_updated','-date_posted']
    
    
    def __str__(self):
        return self.post_title
    

# The following model is developed for direct message function in the app
# Model for conversation between 2 Users
class Thread(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1.username} and {self.user2.username}"
    
# Model for individual message
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        get_latest_by = ['created_at']

    def __str__(self):
        return self.content[:50]

# Abstract Model for User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatar/')
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=20)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.user.username + " 's profile"

# Concrete Model for User Profile (User/ Landlord)
class UserProfile(Profile):
    account_type = 'user'
    

# Concrete Model for User Profile (Realtor)
class RealtorProfile(Profile):
    account_type = 'realtor'
    company = models.CharField(null=True, blank=True, max_length=100)
    