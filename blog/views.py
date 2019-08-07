from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})

@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post-detail',pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html',{'form':form})
	
@login_required
def edit_post(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)	
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post-detail',pk=post.pk)
	else:
		form = PostForm(instance=post)

	return render(request, 'blog/post_edit.html',{'form':form})


def register(request):
	if request.method == 'POST':
		form  = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Hesabınız oluşturuldu')
			return redirect('post_list')
	else:
		form = UserCreationForm()

	return render(request,'blog/register.html',{'form':form})
