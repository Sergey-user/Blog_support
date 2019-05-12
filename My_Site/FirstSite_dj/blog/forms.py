from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
	
	# title = forms.CharField(max_length=50)
	# slug = forms.CharField(max_length=50)

	# title.widget.attrs.update({'class': 'form-field', 'placeholder': 'Enter title'})
	# slug.widget.attrs.update({'class': 'form-field', 'placeholder': 'Enter slug'})

	class Meta:
		model = Tag
		fields = ['title', 'slug']


		widgets = {
			'title': forms.TextInput(attrs={'class':'form-field', 'placeholder': 'Enter title'}),		
			'slug': forms.TextInput(attrs={'class':'form-field', 'placeholder': 'Enter slug'})
			}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError('Slug may not be "Create"')

		return new_slug
	

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'slug', 'body', 'tags']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Enter title'}),
			'slug': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Enter slug'}),
			'body': forms.Textarea(attrs={'class': 'form-field', 'placeholder': 'Enter body', 'id': 'textarea'}),
			'tags': forms.SelectMultiple(attrs={'class': 'form-field','id':'select'})

			# attrs={'class': 'form-field', 'id': 'select'}
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError(' Slug may not be "Create" ')

		return new_slug