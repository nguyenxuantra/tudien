from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import RegistrationForm,ComentForm
from .models import painting,comment

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
        keys = painting.objects.filter(name__contains=searched)
        keys_values = [{'name': key.name, 'discription': key.discription, 'image': key.image.url} for key in keys]
        search_history = request.session.get('search_history', [])
        result_exists = any(searched in result['name'] or searched in result['discription'] for search_result in search_history for result in search_result['keys_values'])

        if not result_exists:
            search_history.append({'searched': searched, 'keys_values': keys_values})
        search_history.reverse()
        request.session['search_history'] = search_history

        return render(request, 'pages/search.html', {'searched': searched, 'keys': keys, 'search_history': search_history})






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