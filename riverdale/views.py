from django.shortcuts import redirect, render


from riverdale.forms import CreateUserForm
from .models import Business, Neighborhood, Post,User,Images
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages



# home
def home(request):
    user=request.user
    neighborhoods=Neighborhood.objects.all()
    users=User.objects.filter()
    context={
        "neighborhoods":neighborhoods,
        "users":users,
        "user":user,
    }
    return render(request,'home.html',context)
# register
def register(request):
    if request.user.is_authenticated:

      return redirect('home')
    else:
    
        form = CreateUserForm()
        if request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        
        context = {'form':form}
      
    return render(request,'register.html',context)

# login
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')

            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}

    return render(request,'login.html',context)

# profile
def profile(request):
    user=request.user
    users=User.objects.filter()

    return render(request,'profile/profile.html',{'users':users,"user":user})

# editprofile
@login_required(login_url='/accounts/login/')
def editprofile(request):
    if request.method == "POST":
        prod = User()
        prod.name = request.POST.get('name'),
        prod.house_no = request.POST.get('house_no')
        prod.contacts = request.POST.get('contacts') 
        prod.email_address = request.POST.get('email_address')
        prod.neighborhood_id = request.POST.get('neighborhood.title')


        prod.save()
        
        return redirect('profile' )
    return render(request,'profile/edit_profile.html')


# neighborhood(phase1,2,3)
def phase(request,id):
    user=request.user
    neighborhoods=Neighborhood.objects.filter(id=id)
    images = Images.objects.filter(neighborhood_id=id)
    posts = Post.objects.filter(neighborhood_id=id)
    businessess=Business.objects.filter(neighborhood_id=id)
    

        
    context={
        'user':user,
        'businessess':businessess,
        'neighborhoods':neighborhoods,
        'images':images,
        "posts":posts,

    }


    return render(request,'types/phase.html',context)

# post

# search

def search(request):
        if "neighborhood" in request.GET and request.GET["neighborhood"]:
            searched_item=request.GET["neighborhood"]
            neighborhood= Neighborhood.search_by_title(searched_item)
            message = f"{searched_item}"


            return render(request, 'search.html',{"message":message,"neighborhood":neighborhood})
        else:
            message = "Kindly input a search term to get any results"
            return render(request,'search.html',{})



#display_search
def display_search(request):

    neighborhood=Neighborhood.objects.all()

    return render(request,'search.html',{"neighborhood":neighborhood})



@login_required(login_url='/accounts/login/')
def logout(request):

    return render(request, 'login.html')