from django.forms import ModelForm
from .models import Book, Author

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = [
			"title",
			"author",
			"price",
			"publish",
		]

class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = [
			"name"
		]