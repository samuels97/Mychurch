from django.shortcuts import render
from django.views import View

class IndexView(View):
	template_file = 'main/index.html'
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
