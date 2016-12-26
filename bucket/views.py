from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import authenticate,logout as auth_logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Item
from .forms import ItemForm,LoginForm

@login_required(login_url='/login/')
def items_list(request):
	items = Item.objects.all().filter(user=request.user).order_by('price')
	return render(request, 'bucket/items_list.html', {'items': items})

@login_required(login_url='/login/')
def item_new(request):
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.id = len(Item.objects.all()) + 1
			item.user = request.user
			item.save()
			return redirect(items_list)
	else:
		form = ItemForm()
	return render(request, 'bucket/item_edit.html', {'form': form})

@login_required(login_url='/login/')
def item_edit(request, id):
	item = get_object_or_404(Item, id=id)
	if request.method == "POST":
		form = ItemForm(request.POST, instance=item)
		if form.is_valid():
			item = form.save(commit=False)
			item.save()
			return redirect(items_list)
	else:
		form = ItemForm(instance=item)
	return render(request, 'bucket/item_edit.html', {'form': form})


@login_required(login_url='/login/')
def item_delete(request, id):
	Item.objects.filter(id=id).delete()
	return redirect(items_list)

def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			username = data.email
			password = data.password
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					auth_login(request, user)
					return redirect(items_list)
	else:
		form = LoginForm()
	return render(request, 'bucket/login.html', {'form': form})

def registration(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			username = data.email
			password = data.password
			try:
				u = User.objects.get(username=username)
			except User.DoesNotExist:
				u = None
			if (not u):
				user = User.objects.create_user(username, None, password)	
				auth_login(request, user)
				return redirect(items_list)
	else:
		form = LoginForm()
	return render(request, 'bucket/registration.html', {'form': form})

def logout(request):
	auth_logout(request)
	return redirect('login')

