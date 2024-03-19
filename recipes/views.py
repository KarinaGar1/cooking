from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


def recipes_home(request):
    recipes = Articles.objects.all()
    return render(request, 'recipes/recipes_home.html', {'recipes': recipes})


def recipes_breakfast(request):
    recipes_b = Articles.objects.filter(kategor="Завтрак")
    return render(request, 'recipes/recipes_breakfast.html', {'recipes_b': recipes_b})


def recipes_lunch(request):
    recipes_l = Articles.objects.filter(kategor="Обед")
    return render(request, 'recipes/recipes_lunch.html', {'recipes_l': recipes_l})


def recipes_dinner(request):
    recipes_d = Articles.objects.filter(kategor="Ужин")
    return render(request, 'recipes/recipes_dinner.html', {'recipes_d': recipes_d})


class Search(ListView):
    template_name = 'recipes/recipes_home.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Articles.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class RecipesDetailView(DetailView):
    model = Articles
    template_name = 'recipes/details_view.html'
    context_object_name = 'article'


class RecipesUpdateView(UpdateView):
    model = Articles
    success_url = '/recipes/'
    template_name = 'recipes/create.html'

    form_class = ArticlesForm


class RecipesDeleteView(DeleteView):
    model = Articles
    success_url = '/recipes/'
    template_name = 'recipes/recipes-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'recipes/create.html', data)