from django.shortcuts import render, redirect
from .models import BlogComment, BlogPost, BlogGallery, BlogReaction, BlogappProfile, BlogMessage, BlogProject
from blog.form import CommentForm, MessageForm, ReplyForm
from django.views import View



def home(request):
    posts = BlogPost.objects.all() 
    gallerys = BlogGallery.objects.all()
    
    #message = BlogMessage.objects.all()
    
    content = {
            'posts': posts [::-1],
            'gallery': gallerys [::-1],
            'profile': BlogappProfile.objects.all(),
            'project': BlogProject.objects.all(),
            'reaction': BlogReaction.objects.all()
    }

    if request.method == "POST":
        form = MessageForm(request.POST)
        formR = reactionForm(request.POST, None)
        if form.is_valid():
            form.save()
            form = MessageForm()
            formR = reactionForm(None)
			#messages.success(request, f' Tua mensagem foi enviada com sucesso !')
            return redirect('home')
        else:
            form = MessageForm()
            formR = reactionForm(None)
            content['form'] = form
            content['formR'] = formR
    else:
        form = MessageForm()
        formR = reactionForm(None)
        content['form'] = form
        content['formR'] = formR        

    return render(request, 'index.html', content)

def reaction(request, post_id):
    posts = BlogPost.objects.all() 
    gallerys = BlogGallery.objects.all()
    
    #message = BlogMessage.objects.all()
    
    content = {
            'posts': posts [::-1],
            'gallery': gallerys [::-1],
            'profile': BlogappProfile.objects.all(),
            'project': BlogProject.objects.all(),
            'reaction': BlogReaction.objects.all()
    }

    if request.method == "POST":
        form = MessageForm(request.POST)
        formR = reactionForm(request.POST, post_id)
        if form.is_valid():
            form.save()
            form = MessageForm()
            formR = reactionForm(post_id)
			#messages.success(request, f' Tua mensagem foi enviada com sucesso !')
            return redirect('home')
        else:
            form = MessageForm()
            formR = reactionForm(post_id)
            content['form'] = form
            content['formR'] = formR
    else:
        form = MessageForm()
        formR = reactionForm(post_id)
        content['form'] = form
        content['formR'] = formR       

    return render(request, 'index.html', content)


def pub(request, post_id):
    comment = BlogComment.objects.filter(parent=None).order_by('-id')
    posts = BlogPost.objects.get(id = post_id)
    

    content = {
        'post_id': post_id,
        'posts': posts,
        'comment': comment
    }
    
    if request.method == "POST":
        form = CommentForm(post_id, request.POST)
        formReply = ReplyForm(post_id, request.POST)
        
        nome = request.POST.get('nome')
        mensagem = request.POST.get('mensagem')
        post = request.POST.get('post')
        parent_id = request.POST.get('parent_id')

        # is_dislike = False

        # for dislike in posts.dislikes.all():
        #     if dislike == request.user:
        #         is_dislike = True
        #         break

        # if is_dislike:
        #     posts.dislikes.remove(request.user)

        # is_like = False

        # for like in posts.likes.all():
        #     if like == request.user:
        #         is_like = True
        #         break

        # if not is_like: 
        #     posts.likes.add(request.user)
        
        # if is_like:
        #     posts.likes.remove(request.user)



        if form.is_valid() or formReply.is_valid:
            if parent_id:
                co_set = BlogComment.objects.get(id=parent_id)
                reply = BlogComment.objects.create(nome=nome, mensagem=mensagem, post=post, parent=co_set)
                reply.save()
            else:
                form.save()
                form = CommentForm(post_id)
                content['form'] = form
                content['formReply'] = formReply
			#messages.success(request, f' Tua mensagem foi enviada com sucesso !')
            return redirect('pub', post_id)
        else:
            form = CommentForm(post_id)
            formReply = ReplyForm(post_id)
            content['form'] = form
            content['formReply'] = formReply
    else:
        form = CommentForm(post_id)
        formReply = ReplyForm(post_id)
        content['form'] = form
        content['formReply'] = formReply          

    return render(request, 'page.html', content)

# def reply(request, co_id, post_id):
    replies = BlogCommentReply.objects.all()
    comment = BlogComment.objects.all()
    posts = BlogPost.objects.get(id = post_id)

    content = {
        'replies': replies,
        'post_id': post_id,
        'co_id': co_id,
        'posts': posts,
        'comment': comment
    }
    
    if request.method == "POST":
        form = CommentForm(post_id, request.POST)
        formReply = ReplyForm(co_id,request.POST)
      
        if form.is_valid() or formReply.is_valid():
            form.save()
            formReply.save()
            form = CommentForm(post_id)
            formReply = ReplyForm(co_id)
            content['form'] = form
            content['formReply'] = formReply 
			#messages.success(request, f' Tua mensagem foi enviada com sucesso !')
            return redirect('pub', post_id)
        else:
            form = CommentForm(post_id)
            formReply = ReplyForm(co_id)
            content['form'] = form
            content['formReply'] = formReply 
    else:
        form = CommentForm(post_id)
        formReply = ReplyForm(co_id)
        content['form'] = form
        content['formReply'] = formReply           

    return render(request, 'page.html', content)

