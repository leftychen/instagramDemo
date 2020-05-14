from annoying.decorators import ajax_request
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from Insta.models import Post,Like
from Insta.forms import CustomizedUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PostsView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title','image']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']
    login_url = 'login'


# function for create delete html
# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'post_delete.html'
#     success_url = reverse_lazy('posts')
class SignUp(CreateView):
    form_class = CustomizedUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# functions for modal delete
def delete_post(request, id=None):
    post_to_delete = Post.objects.get(pk=id)
    post_to_delete.delete()
    return redirect(reverse_lazy('posts'))

# function for like
@ajax_request
def add_like(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
