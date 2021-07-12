from django.shortcuts import render, redirect
from .models import BlogComment, BlogPost, BlogGallery, BlogappProfile, BlogMessage, BlogProject
from blog.form import CommentForm, MessageForm
from django.views import View



def home(request):
    posts = BlogPost.objects.all() 
    gallerys = BlogGallery.objects.all()
    #message = BlogMessage.objects.all()
    
    content = {
            'posts': posts [::-1],
            'gallery': gallerys [::-1],
            'profile': BlogappProfile.objects.all(),
            'project': BlogProject.objects.all()
    }

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
			#messages.success(request, f' Tua mensagem foi enviada com sucesso !')
            return redirect('home')
        else:
            form = MessageForm()
            content['form'] = form
    else:
        form = MessageForm()
        content['form'] = form        

    return render(request, 'index.html', content)


def pub(request, post_id):
    comment = BlogComment.objects.all()
    posts = BlogPost.objects.get(id = post_id)

    content = {
        'post_id': post_id,
        'posts': posts,
        'comment': comment
    }
    
    if request.method == "POST":
        form = CommentForm(post_id, request.POST)

        if form.is_valid():
            form.save()
            form = CommentForm(post_id)
            content['form'] = form 
			#messages.success(request, f' Tua mensagem foi enviada com sucesso !')
            return redirect('pub', post_id)
        else:
            form = CommentForm(post_id)
            content['form'] = form
    else:
        form = CommentForm(post_id)
        content['form'] = form          

    return render(request, 'page.html', content)
