
from django.shortcuts import render, redirect

class ObjectCreateMixin:

	model_form = None
	template = None

	def get(self, request):
		form = self.model_form()
		return render(request, self.template, context={'form': form})

	def post(self, request):
		bound_form = self.model_form(request.POST)

		if bound_form.is_valid():
			new_object = bound_form.save()
			return redirect(new_object)
		return render(request, self.template, context={'form': bound_form})