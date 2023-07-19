from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from .forms import RegistrationForm,comentForm
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
        
        # Lấy danh sách lịch sử tìm kiếm từ session
        context_results = request.session.get('context_results', [])
        
        # Thêm từ khóa đã tìm kiếm vào danh sách
        context_results.append(searched)
        
        # Giới hạn số lượng mục trong danh sách lịch sử tìm kiếm (ví dụ: giữ 5 mục gần nhất)
        context_results = context_results[-5:]
        
        # Lưu danh sách lịch sử tìm kiếm vào session
        request.session['context_results'] = context_results
        return render(request, 'pages/search.html', {'searched': searched, 'keys': keys, 'context_results': context_results})

def painting_detail(request, pk):
    painting_instance = get_object_or_404(painting, pk=pk)
    form = comentForm()
    if request.method == 'POST':
        form = comentForm(request.POST, author=request.user, painting=painting_instance)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    return render(request, "pages/painting.html", {"painting": painting_instance, "form": form})

