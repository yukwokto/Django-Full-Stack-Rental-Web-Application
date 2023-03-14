from django.shortcuts import render, redirect
from .models import Rental, Category, Thread, Message, UserProfile, RealtorProfile
from .post_ad import RentalForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .enquiry_form import MessageForm
from .registration_form import UserForm, UserProfileForm, RealtorProfileForm
from django.core.paginator import Paginator
import re

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

# create operation: create an advertisement
@login_required(login_url='login') # remember to remove /
def post_ad(request):
    form = RentalForm()
    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES)  # grab the content of the form
        if form.is_valid():
            unit = form.save(commit=False)
            unit.landlord = request.user
            unit.save()
            return redirect('listing')
    context = {'form': form}
    return render(request, 'base/post_ad.html', context)


# update operation: update an advertisement
@login_required(login_url='login')
def update_ad(request, pk):
    unit = Rental.objects.get(id=pk)
    form = RentalForm(instance=unit)
    
    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('listing')
    context = {'form': form}
    return render(request, 'base/post_ad.html', context)

# delete operation: delete an advertisement
@login_required(login_url='login')
def delete_ad(request, pk):
    ad = Rental.objects.get(id=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('listing')
    return render(request, 'base/delete.html', {'ad': ad})


def listing(request):
    # implementation of serach + budget filter function
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    min_budget = request.GET.get('minbudget') if request.GET.get('minbudget') else 0
    max_budget = request.GET.get('maxbudget') if request.GET.get('maxbudget') else 10000000000

    try:
        cur_listings = Rental.objects.filter(rent__gte=int(min_budget), rent__lte=int(max_budget))
    except:
        messages.error(request, 'Please enter a valid range')
        cur_listings = Rental.objects.filter(rent__gte=0, rent__lte=10000000000000000)
        
    cur_listings = cur_listings.filter(
            Q(post_title__icontains = q) |
            Q(address__icontains = q) |
            Q(rent__icontains = q) |
            Q(category__type__icontains = q) |
            Q(landlord__username__icontains = q)
        )
    
    a = request.GET.get('a') if request.GET.get('a') != None else ''
    cur_listings = cur_listings.filter(
        Q(category__type__icontains = a)
    )
    
    # show the major rental categories
    types = Category.objects.all()[:7]
    
    # show the count of available listings
    ava = cur_listings.count()
    
    # show some of the featured realtors
    featured_realtors = RealtorProfile.objects.all().order_by('?')[:3]
    
    # add pagination
    p = Paginator(cur_listings, 5)
    page = request.GET.get('page')
    cur_listings = p.get_page(page)
    
    # build the URL query string with the search and filter parameters
    query_string = ''
    if q:
        query_string += 'q=' + q + '&'
    if min_budget:
        query_string += 'minbudget=' + str(min_budget) + '&'
    if max_budget:
        query_string += 'maxbudget=' + str(max_budget) + '&'
    if a:
        query_string += 'a=' + a + '&'
    
    context = {'cur_listings': cur_listings, 'types': types, 'ava': ava,
               'featured_realtors': featured_realtors, 'query_string': query_string}
    
    return render(request, 'base/listing.html', context)

# show the unit from the ad
# also allow user to send enquiry message to the landlord
def unit(request, pk):
    unit = Rental.objects.get(id=pk)
    landlord = unit.landlord # get the name of the landlord
    # if user wants to make an enquiry to the landlord
    form = MessageForm()
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        thread = Thread.objects.filter(user1=request.user, user2=landlord) | Thread.objects.filter(user1=landlord, user2=request.user)
        if thread.exists():
            thread = thread.first()
        else:
            thread = Thread.objects.create(user1=request.user, user2=landlord)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = landlord
            message.thread = thread
            message.save()
            return redirect('unit', pk)
        else:
            pass
        
    context = {'unit': unit, 'form': form}
    return render(request, 'base/unit.html', context)


def about(request):
    return render(request, 'base/about.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('listing')
    
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            pass
        
        user = authenticate(request, username=username, password=password)
        
        # returns a User object if the credentials are valid for the backend.
        if user is not None:
            login(request, user)
            return redirect('listing')
        else:
            messages.error(request, 'Incorrect Username or password')
        
    context = {'page': page}
    return render(request, 'base/login_form.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

# Allows different type of users to create their specific account
def selectAccountType(request):
    context = {}
    return render(request, 'base/select_account_type.html', context)

# create User Type  Account 
def registerUserAccount(request):
    account_type = 'User'
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('listing')

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form, 'account_type': account_type}
    return render(request, 'base/create_account.html', context)

def registerRealtorAccount(request):
        account_type = 'Realtor'
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = RealtorProfileForm(request.POST, request.FILES)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                login(request, user)
                return redirect('listing')

        else:
            user_form = UserForm() 
            profile_form = RealtorProfileForm()

        context = {'user_form': user_form, 'profile_form': profile_form, 'account_type': account_type}
        return render(request, 'base/create_account.html', context)

# for user to check their enquiry message
@login_required(login_url='login')
def threadPage(request):
    threads = Thread.objects.filter(user1=request.user) | Thread.objects.filter(user2=request.user)
    context = {'threads': threads}
    return render(request, 'base/threads.html', context)


# for landlord to view the actual message
@login_required(login_url='login')
def messagePage(request, username):
    
    # displaying the message
    user = User.objects.get(username=username)
    thread = Thread.objects.filter(user1=request.user, user2=user) | Thread.objects.filter(user1=user, user2=request.user)

    try:
        chat_with = ''
        if thread.first().user1.username == request.user.username:
            chat_with = thread.first().user2.username
        else:
            chat_with = thread.first().user1.username
        
        if thread.exists():
            thread = thread.first()
            messages = Message.objects.filter(thread=thread)
    except:
        pass
    
    # for user to reply message
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        thread = Thread.objects.filter(user1=request.user, user2=user) | Thread.objects.filter(user1=user, user2=request.user)
        if thread.exists():
            thread = thread.first()
        else:
            thread = Thread.objects.create(user1=request.user, user2=user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = user
            message.thread = thread
            message.save()
            return redirect('message_page', user.username)
        else:
            pass
    context = {'messages': messages, 'form': form, 'chat_with': chat_with}
    return render(request, 'base/enquiry_message.html', context)

# user profile page
@login_required(login_url='login')
def accountProfile(request, pk):
    user = User.objects.get(id=pk)
    account_type = ''
    
    try:
        user_profile = UserProfile.objects.get(user=user)
        account_type = 'User'
    except:
        user_profile = RealtorProfile.objects.get(user=user)
        account_type = 'Realtor'
    
    current_listings = Rental.objects.filter(landlord = user)
    
    
    # leaving user/ realtor a message on their profile page
    form = MessageForm()
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        thread = Thread.objects.filter(user1=request.user, user2=user) | Thread.objects.filter(user1=user, user2=request.user)
        if thread.exists():
            thread = thread.first()
        else:
            thread = Thread.objects.create(user1=request.user, user2=user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = user
            message.thread = thread
            message.save()
            messages.success(request, 'Message has been sent successfully.')
            return redirect('profile_page', pk)
        else:
            pass
        
    context = {'user': user, 'profile': user_profile, 'account_type': account_type,
               'current_listings': current_listings, 'form': form}
    return render(request, 'base/profile.html', context)


# allow user to update their profile
@login_required(login_url='login')
def updateProfile(request):
    user = User.objects.get(username = request.user)
    username_pattern = r'^[a-zA-Z0-9]+$'
    
    if request.method == 'POST':
        new_username = request.POST.get('newUsername') if request.POST.get('newUsername') != None \
            and re.match(username_pattern, request.POST.get('newUsername')) \
            else request.user.username
        
        try:
            profile = UserProfile.objects.get(user=request.user)
            profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
            
            if profile_form.is_valid():
                profile_form.save()
                user.username = new_username
                user.save()
                return redirect('profile_page', request.user.id)
            
        except:
            profile = RealtorProfile.objects.get(user=request.user)
            profile_form = RealtorProfileForm(request.POST, request.FILES, instance=profile)
            
            if profile_form.is_valid():
                profile_form.save()
                user.username = new_username
                user.save()
                return redirect('profile_page', request.user.id)
            
    else:
        
        try:
            profile = UserProfile.objects.get(user=request.user)
            profile_form = UserProfileForm(instance=profile)
        
        except: 
            profile = RealtorProfile.objects.get(user=request.user)
            profile_form = RealtorProfileForm(instance=profile)
            
    context = {'profile_form': profile_form}
    
    return render(request, 'base/profile_update.html', context)