from django.shortcuts import render
from django.views import View
from django.urls import request
from django.http import httpResponseRedirect

class IndexView(View):
	template_file = 'main/index.html'
	context = {}
	def get(self, request, *args, **kwargs):
		return render(request, self.template_file, {})

class AboutView(IndexView):
    template_file = 'main/article.html'

class ContactView(IndexView):
    template_file = 'main/contact.html'

class TravelView(IndexView):
    template_file = 'main/travel.html'

class ArticleView(IndexView):
    template_file = 'main/article.html'

class PrivacyPolicyView(IndexView):
    template_file = 'main/privacy-policy.html'

class TermsConditionsView(IndexView):
    template_file = 'main/terms-conditions.html'

class PageNotFoundView(IndexView):
    template_file = 'main/404.html'

# saving message from outer user
class ContactMessageView(IndexView):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # checking for spaces and unwanted values
        all_variables = [name, email, subject, message]
        new_variable = ""
        for x in all_variables:
            for v in x:
                if v.isspace():
                    new_variable.append()
                if v.isalpha():
                    new_variable.append()
                else:
                    error = "Only letters allowed in name"
            if error != "":
                break



    else:
        template_file = 'main/index.html'
        context = {}
