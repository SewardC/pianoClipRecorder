from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
import json
from .forms import UserForm, AuthenticationForm
from django.template.context_processors import csrf
from django.contrib import auth

# Create your views here.

def records(request):
	return render(request, 'pianoClipRecords/records.html', {})

class AuthenticationView(View):
	form_class = AuthenticationForm
	template_name = 'pianoClipRecords/index_form.html'
	#def post(self, request):
	#	data = json.load(request.POST)
	#	username = request.POST.get('username', False)
	#	password = request.POST.get('password', False)	
	#	user = authenticate(username = username, password = password)
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
		
	def post(self, request):
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('pianoClipRecords:records')

		return render(request, self.template_name, {'form': form})

class UserFormView(View):
	form_class = UserForm
	template_name = 'pianoClipRecords/registration_form.html'

	# black form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# return User objects if credentials are correct
			user = authenticate(username=username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('pianoClipRecords:records')

		return render(request, self.template_name, {'form': form})