from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
                  path('', views.index, name='index'),
                  path('Portfolio/', views.Portfolio, name='Portfolio'),
                  path('PortfolioPage/<int:id>/', views.singlePortfolio, name='PortfolioPage'),
                  path('weblogs/', views.weblogs, name='weblogs'),
                  path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
                  path('contactUs/', views.about, name='contactUs'),
                  path('PortfolioPage/', views.singlePortfolio, name='PortfolioPage'),
                  path('search/', views.search_results, name='search_results'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
