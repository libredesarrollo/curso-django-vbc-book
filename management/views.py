from dataclasses import fields
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic import DetailView, ListView
from django.views import View

from .models import Book
from .forms import BookForm

class BookSaveFormView(FormView):
    template_name='book/save.html'
    form_class=BookForm
    success_url='/book/namagement/save/success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BookUpdateFormView(UpdateView):
    model=Book
    template_name='book/save.html'
    #fields = ['name', 'author']
    form_class = BookForm
    success_url='/book/namagement/save/success'

class BookCreateFormView(CreateView):
    model=Book
    template_name='book/save.html'
    fields = ['name', 'author']
    #form_class = BookForm
    success_url='/book/namagement/save/success'

class BookDeleteFormView(DeleteView):
    model=Book
    template_name='book/delete.html'
    success_url='/book/namagement/save/success'

class BookDetailFormView(DetailView):
    model=Book
    context_object_name="book" #object
    template_name='book/detail.html'
class BookListFormView(ListView):
    model=Book
    context_object_name="books" #object_list
    template_name='book/index.html'

class BookSaveFormSuccessView(View):
    def get(self, request):
        #return render(request,"book/save.html")
        return HttpResponse("El libro se creo! se feliz :)")

