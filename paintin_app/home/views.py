from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import RegistrationForm,ComentForm,PaintingForm
from .models import painting,comment
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'pages/home.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'pages/register.html',{'form':form})
def dangnhap(request):
    return render(request,'pages/dangnhap.html')
def search(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        style = request.POST.get("style")
        topic = request.POST.get("topic")

        keys = painting.objects.filter(name__contains=searched)
        if style:
            keys = keys.filter(style__icontains=style)
        if topic:
            keys = keys.filter(topic__icontains=topic)

        keys_values = [{'name': key.name, 'discription': key.discription, 'image': key.image.url} for key in keys]
        # Initialize search_history as an empty list
        search_history = request.session.get('search_history', [])
        
        # Check for duplicates
        result_exists = any(searched in result['name'] or searched in result['discription'] for search_result in search_history for result in search_result['keys_values'])

        if not result_exists:
            
            search_history.append({'searched': searched, 'keys_values': keys_values})
            search_history.reverse()
            request.session['search_history'] = search_history
        return render(request, 'pages/search.html', {'searched': searched, 'keys': keys, 'search_history': search_history, 'style': style, 'topic': topic})
    return render(request, 'pages/search.html')




def search_history(request):
    search_history = request.session.get('search_history', {})
    return render(request, 'pages/search_history.html', {'search_history': search_history})

@login_required
def painting_detail(request, pk):
    painting_instance = get_object_or_404(painting, pk=pk)
    form = ComentForm()
    if request.method == 'POST':
        form = ComentForm(request.POST, author=request.user, painting=painting_instance)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    return render(request, "pages/painting.html", {"painting": painting_instance, "form": form})


def painting_list(request):
    paintings = painting.objects.all()
    return render(request, 'pages/painting_list.html', {'paintings': paintings})

def add_painting(request):
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('painting_list')
    else:
        form = PaintingForm()
    return render(request, 'pages/add_painting.html', {'form': form})

def edit_painting(request, pk):
    painting_detail = painting.objects.get(pk=pk)
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES, instance=painting_detail)
        if form.is_valid():
            form.save()
            return redirect('painting_list')
    else:
        form = PaintingForm(instance=painting_detail)
    return render(request, 'pages/edit_painting.html', {'form': form})

def delete_painting(request, pk):
    painting_detail = painting.objects.get(pk=pk)
    if request.method == 'POST':
        painting_detail.delete()
        return redirect('painting_list')
    return render(request, 'pages/delete_painting.html', {'painting': painting_detail})

def report_issue(request):
    return render(request, 'pages/report_issue.html') 

def add_related_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        discription = request.POST.get('discription')
        image = request.FILES.get('image')

        new_info = painting(name=name, discription=discription, image=image)
        new_info.save()

    # Lấy thông tin tất cả các bản ghi
    related_paintings = painting.objects.all()

    return render(request, 'pages/add_related_info.html', {'related_paintings': related_paintings})

