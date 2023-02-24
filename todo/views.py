from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import TodoDataForm
from .models import TodoData
from django.contrib.auth.decorators import login_required




# Create your views here.

@login_required(login_url='login') #DECORATOR TO PREVENT UNLOGGED USER FROM ACCESSING HOME PAGE USING MANUAL URL , IT WILL REDIRECT USER TO LOGIN AND WILL NOT GIVE ACCESS TO HOME PAGE WITHOUT AUTHENTICATING.
def todo_details(request):
    if request.user.is_authenticated:  #to get authenticated user
        user = request.user  #store the auth user in user var
        todos = TodoData.objects.filter(user=user).order_by('-status')  #pass that user in user= field , so it loads all the datas or todos of that passed user (filtering) (similar pk-id)  
                                                                        #use '-' sign to reverse order for normal ordering use name without - sign
        context = {"todos" : todos}

        #search_code
        search_input = request.GET.get('search-area') or ''
        if search_input:
            context['todos']=context['todos'].filter(title__startswith=search_input)
            # context['todos']=context['todos'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        

        return render(request,'todo_details.html',context=context)
    
    
    # else:
    #     return HttpResponse("404") - if no user logged in user cannot get access to home page if though they try to access using manual url or we can set this using decorators

@login_required(login_url='login') #PREVENT UNLOGGED USER FROM ADDING TODOS SAME AS ABOVE!!!
def add_todo(request):
    if request.method == 'GET':
        form = TodoDataForm()
        context = { "form" : form }
        return render(request,'todo_list.html',context=context)
    else:
        if request.user.is_authenticated:
            user = request.user
            form = TodoDataForm(request.POST)
            context = { "form" : form }
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                #print(form.cleaned_data)
                return redirect('todo_details')
            else:
                return render(request,'todo_list.html',context=context)

@login_required(login_url='login')
def update_todo(request,id):
    if request.method == 'GET':
        user_todo = TodoData.objects.get(pk=id)
        form = TodoDataForm(instance=user_todo)
        return render(request,'todo_list.html',{'form':form})
    else:
        user_todo = TodoData.objects.get(pk=id)
        form = TodoDataForm(request.POST,instance=user_todo)
        if form.is_valid():
            form.save()
        return redirect('todo_details')


    # todo = TodoList.objects.get(pk=id)
    # form = TodoForm(instance=todo)
    # return render(request,'todo_list.html',{'form':form})

@login_required(login_url='login')
def delete_todo(request,id):
    TodoData.objects.get(pk=id).delete()
    return redirect('todo_details')

def userlogin(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = { "form" : form }
        return render(request,'login.html',context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        context = { "form" : form }
        if form.is_valid():
            username = form.cleaned_data.get('username') # use when we use builtin forms 
            password = form.cleaned_data.get('password') # to get data from builtin form we use and match and check , can use req.POST('username') if we use custom form
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('todo_details')
        else:
            return render(request,'login.html',context=context)

def userlogout(request):
    logout(request)
    return redirect('login')


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'signup.html', {"form" : form })
 