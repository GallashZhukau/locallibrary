from django.shortcuts import render

# Create your views here.


from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_genre = Genre.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context


    num_authors=Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
            'num_visits':num_visits}, # num_visits appended
    )


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    template_name = "book_list.html"
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "book_detail.html"




class AuthorListView(generic.ListView):
    model = Author
    template_name = "author_list.html"
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "author_detail.html"



