from django.shortcuts import render
from django.http import HttpResponse

from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 1
    # context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='re')[:5] # Get 5 books containing the title war
    # template_name = 'catalog/book_list.html'  # Specify your own template name/location

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='r')[:5] # Get 5 books containing the title war

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


class BookDetailView(generic.DetailView):
    model = Book

    # def book_detail_view(request,pk):
    # 	try:
    #     	book_id=Book.objects.get(pk=pk)
    # 	except Book.DoesNotExist:
    #     	raise Http404("Book does not exist")

    # 	#book_id=get_object_or_404(Book, pk=pk)
    
    # 	return render(
    #     	request,
    #     	'catalog/book_detail.html',
    #     	context={'book':book_id,}
    # 	)        

class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 1


class AuthorDetailView(generic.DetailView):
	model = Author

	# def author_detail_view(request,pk):
	# 	try:
 #        	author_id=Author.objects.get(pk=pk)
 #    	except Author.DoesNotExist:
 #        	raise Http404("Author does not exist")

 #    		#book_id=get_object_or_404(Book, pk=pk)
    
 #    	return render(
 #        	request,
 #        	'catalog/author_detail.html',
 #        	context={'author':author_id,}
 #    	)         

