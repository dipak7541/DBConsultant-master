from django.urls import path
from django.views.generic import TemplateView
from .views import index

app_name = 'core'
urlpatterns = [
    path('', index, name='Home-page'),
    path("detailservice/", TemplateView.as_view(template_name="Services/detailedservices.html"), name="detailservice"),
    path("department-details/", TemplateView.as_view(template_name="Department/departments_info.html"),name="departmentdetails"),
    path("about/", TemplateView.as_view(template_name="Abouts/about.html"),name="about"),

]
