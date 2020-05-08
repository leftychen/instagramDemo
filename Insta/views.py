from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from Insta.models import Post


class PostsView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']


# function for create delete html
# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'post_delete.html'
#     success_url = reverse_lazy('posts')


# functions for modal delete
def delete_post(request, id=None):
    post_to_delete = Post.objects.get(pk=id)
    post_to_delete.delete()
    return redirect(reverse_lazy('posts'))
