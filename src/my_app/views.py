from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookForm, AuthorForm
from .models import Book, Author
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json

def BookCreate(request):
	form = BookForm(request.POST or None)
	if form.is_valid():
		instance = form.save()		
		return HttpResponseRedirect("/")
	return render(request, "book_form.html", {"form" : form,})

def AuthorCreatePopup(request):
	form = AuthorForm(request.POST or None)
	if form.is_valid():
		instance = form.save()

		## Change the value of the "#id_author". This is the element id in the form
		
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))
	
	return render(request, "author_form.html", {"form" : form})

def AuthorEditPopup(request, pk = None):
	instance = get_object_or_404(Author, pk = pk)
	form = AuthorForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save()
		
		## Change the value of the "#id_author". This is the element id in the form
		
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))

	return render(request, "author_form.html", {"form" : form})

@csrf_exempt
def get_author_id(request):
	if request.is_ajax():
		author_name = request.GET['author_name']
		author_id = Author.objects.get(name = author_name).id
		data = {'author_id':author_id,}
		return HttpResponse(json.dumps(data), content_type='application/json')
	return HttpResponse("/")