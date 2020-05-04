from django.views.generic import TemplateView
# inherited from Hello Template new
class HelloWorld(TemplateView):
    template_name = 'helloworld.html'
