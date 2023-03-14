from django.contrib import admin
from .models import Category, Rental, Thread, Message, UserProfile, RealtorProfile


# Register your models here.
admin.site.register(Category)
admin.site.register(Rental)
admin.site.register(Thread)
admin.site.register(Message)
admin.site.register(UserProfile)
admin.site.register(RealtorProfile)


