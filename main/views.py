from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import NewCategoryForm, NewItemForm

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    return render(request, 'main/home.html', {'categorys': Category.objects.all()})

def about(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    return render(request, 'main/about.html', {})

def new_category(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    if not request.user.groups.filter(name='admins').exists():
        return render(request ,'users/access_denied.html', {})
    if request.method == 'POST':
        form = NewCategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewCategoryForm()
        return render(request, 'main/new_category.html', {'form': form})

def category_items(request, category_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    category = Category.objects.get(id=category_id)
    items = category.product_set.all()
    return render(request, 'main/category_items.html', {'category': category, 'items': items})

def new_item(request, category_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    if not request.user.groups.filter(name='admins').exists():
        return render(request ,'users/access_denied.html', {})
    form = NewItemForm()
    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        form = NewItemForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)  # Don't save to the database yet
            product.category = category       # Assign the category
            product.save()                    # Now save to the database
            return redirect('category-items', category.id)

    return render(request, 'main/new_item.html', {'form': form, 'category': category})

def edit_item(request, category_id, item_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    if not request.user.groups.filter(name='admins').exists():
        return render(request ,'users/access_denied.html', {})
    category = Category.objects.get(id=category_id)
    item = Product.objects.get(id=item_id, category=category)
    form = NewItemForm(instance=item)

    if request.method == 'POST':
        form = NewItemForm(request.POST, instance=item)

        if form.is_valid():
            product = form.save(commit=False)  # Don't save to the database yet
            product.category = category       # Assign the category
            product.save()                    # Now save to the database
            return redirect('category-items', category.id)

    return render(request, 'main/edit_item.html', {'form': form, 'category': category, 'item': item,})

def delete_item(request, category_id, item_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    if not request.user.groups.filter(name='admins').exists():
        return render(request ,'users/access_denied.html', {})
    category = Category.objects.get(id=category_id)
    item = Product.objects.get(id=item_id, category=category)
    item.delete()
    return redirect('category-items', category.id)

def edit_category(request, category_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    if not request.user.groups.filter(name='admins').exists():
        return render(request ,'users/access_denied.html', {})
    category = Category.objects.get(id=category_id)
    form = NewCategoryForm(instance=category)

    if request.method == 'POST':
        form = NewCategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()
            return redirect('category-items', category.id)

    return render(request, 'main/edit_category.html', {'form': form, 'category': category})

def delete_category(request, category_id):
    if not request.user.is_authenticated:
        return render(request, 'users/login_required.html')
    if not request.user.groups.filter(name='admins').exists():
        return render(request ,'users/access_denied.html', {})
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('home')
