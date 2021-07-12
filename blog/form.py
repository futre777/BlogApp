from os import initgroups
from django import forms
from django.http import request  
from blog.models import BlogMessage, BlogComment, BlogPost

class MessageForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)
		self.fields['nome'].widget.attrs.update({'class':'form-control', 'id':'subject'})
		self.fields['email'].widget.attrs.update({'type': 'email', 'class':'form-control', 'id':'email'})
		self.fields['mensagem'].widget.attrs.update({'id':'message','cols':'30', 'rows':'7', 'class':'form-control', 'placeholder':'Escreve teus notes ou perguntas aqui...', 'style': 'height : 12px'})

	class Meta:
		model = BlogMessage
		fields = ['nome', 'email', 'mensagem'] 

class CommentForm(forms.ModelForm):
	def __init__(self, post_id=None, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		p = BlogPost.objects.get(id=post_id)
		self.fields['nome'].widget.attrs.update({'class':'form-control', 'id':'subject', 'placeholder':'Nome'})
		self.fields['mensagem'].widget.attrs.update({'id':'message','cols':'30', 'rows':'2', 'class':'form-control', 'placeholder':'Escreve aqui ..'})
		self.fields['post'] = forms.IntegerField(initial=p.id)
		self.fields['post'].widget = forms.HiddenInput()
		
	class Meta:
		model = BlogComment
		fields = ['nome', 'mensagem', 'post'] 

