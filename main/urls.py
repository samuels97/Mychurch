from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.IndexView.as_view(), name="main"),
	path('about/', views.AboutView.as_view(), name="about"),
	path('travel/', views.TravelView.as_view(), name="travel"),
	path('article/', views.ArticleView.as_view(), name="article"),
	path('privacy-policy/', views.PrivacyPolicyView.as_view(), name="privacy-policy"),
	path('terms-conditions/', views.TermsConditionsView.as_view(), name="terms-conditions"),
    path('404/', views.PageNotFoundView.as_view(), name="404"),
    path('contact/', views.ContactView.as_view(), name="contact"),

    # saving message from outer user
    path('save-message/', views.ContactMessageView.as_view(), name="save-message"),
]