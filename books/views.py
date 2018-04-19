from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


# Create your views here.
def search_form(request):
    return render(request, 'searchform.html')

# def search(request):
#     # if 'q' in request.GET:
#     #     message = ['You searched for: %r' % request.GET['q']]
#     # else:
#     #     message = ['You submitted an empty form.']
#     # return render(request, 'searchresult.html', {'title': "Book Search Result", 'head': "Search Result", 'object': message})
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         books = Book.objects.filter(title__icontains=q)
#         return render(request, 'searchresult.html', {'title': "Book Search Result", 'head': "Search Result", 'query' : q, 'books' : books})
#     else:
#         return render(request, 'searchform.html', {'error': True})

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'searchresult.html',{'books': books, 'query': q})
    #return
    return render(request, 'searchform.html',{'errors': errors})