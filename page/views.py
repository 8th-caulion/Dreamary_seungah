from django.shortcuts import render, get_object_or_404, redirect
from .models import Designer

def home(request):
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designers})

def introduce(request):
    return render(request, 'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk = designer_id) #값이 존재하면 담고 리턴 아니면 404에러
    return render(request, 'detail.html', {'designer' : designer})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        post = Designer()
        post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()

        return redirect('detail', post.id)

def update(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)

    if request.method == 'POST':
        post = Designer()
        post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()
        # 결과를 바로 봐야 좋겠져?

        return redirect('detail', post.id)
    else:
        return render(request, 'update.html', {'designer' : post})
        # new와 다르게 이미 있는 객체를 가져와서 정보를 띄워놓고 사용자가 수정해야해서 post에 넣어놨기 때문에!


def delete(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)
    post.delete()

    return redirect('home')