from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index , name='landingPage'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('allservices', views.allServices, name='allservices'),
    path('blog', views.blog, name='blog'),
    path('blogSingle/<str:pk>', views.blogSingle, name='blogSingle'),

    path('contactUs', views.contactUs, name='contactUs'),

    path('audit_And_Non_Assurance_Services',views.audit_And_Non_Assurance_Services, name='audit_And_Non_Assurance_Services'),
    path('tax_Advisory_Services',views.taxAdvisoryServices, name='tax_Advisory_Services'),
    path('accounting_and_finance_Services',views.accounting_and_finance_Services, name='accounting_and_finance_Services'),
    path('business_Governance_Advisory',views.business_Governance_Advisory, name='business_Governance_Advisory'),
    path('company_secretarial_services', views.company_secretarial_services, name='company_secretarial_services' ),
    path('management_Consulting_services', views.management_Consulting_services, name='management_Consulting_services' ),
    path('IT_Consultancy_services', views.it_Consultancy_services, name='IT_Consultancy_services' ),

    path('send_email', views.send_email, name='send_email'),
    path('pdf_detail/', views.pdf_detail, name='pdf_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)