from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import (
    Topbar,
    NavigationBar,
    ImageSlider,
    SlideDashboardSection,
    OurTeam_AboutUs,
    PartnerAndBrands,
    WhyYouUsFeature_Home,
    Testimonial,
    AboutUs,
    Footer,
    TopFooter,
    audit_And_Non_Assurance_contact,
    audit_And_Non_Assurance_team,
    taxadvisory_contact,
    taxadvisory_team,
    accounting_and_finance_contact,
    accounting_and_finance_team,
    Office,
    BlogPost,
)

def index(request):
      # You can customize this response

    topbar_data = Topbar.objects.first()
    navigation_bar_data = NavigationBar.objects.first()
    sliders = ImageSlider.objects.all()
    slideDashboard = SlideDashboardSection.objects.all()
    team_members = OurTeam_AboutUs.objects.all()
    partners = PartnerAndBrands.objects.all()
    whyYouUsFeatures = WhyYouUsFeature_Home.objects.all()
    testimonials = Testimonial.objects.all()
    about_us_instance = AboutUs.objects.first()
    footer_instance = Footer.objects.first() 
    topfooter = TopFooter.objects.first()
    
    context = {
        'topbar_data': topbar_data,
        'navigation_bar_data': navigation_bar_data,
        'sliders': sliders,
        'slideDashboard': slideDashboard,
        'about_us_instance': about_us_instance,
        'team_members': team_members,
        'partners': partners,
        'whyYouUsFeatures': whyYouUsFeatures,
        'testimonials': testimonials,
        'footer_instance': footer_instance,
        'topfooter': topfooter,
    }

    
    return render(request, 'Mega Consulting-Website/index-3.html', context)


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        print(name)
        print(email)

        # Validate form data
        if not name or not email or not phone or not note:
            return HttpResponse('Please fill in all required fields.')

        subject = f'New Inquiry from {name}'
        message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {note}'
        from_email = email  # Use the sender's email as the "from_email" address
        recipient_list = ['iimanishimweinnocent@gmail.com']  # Update with recipient's email address

        try:
            send_mail(subject, message, from_email, recipient_list)
            return HttpResponse('Email sent successfully.')
        except Exception as e:
            return HttpResponse(f'Error occurred: {e}')

    return render(request, 'Mega Consulting-Website/index-3.html')

def aboutUs(request):
    navigation_bar_data = NavigationBar.objects.first()
    whyYouUsFeatures = WhyYouUsFeature_Home.objects.all()
    partners = PartnerAndBrands.objects.all()
    team_members = OurTeam_AboutUs.objects.all()
    about_us_instance = AboutUs.objects.first()
    footer_instance = Footer.objects.first() 
    topfooter = TopFooter.objects.first()
    testimonials = Testimonial.objects.all()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'whyYouUsFeatures': whyYouUsFeatures,
        'partners': partners,
        'team_members': team_members,
        'about_us_instance': about_us_instance,
        'footer_instance': footer_instance,
        'topfooter': topfooter,
        'testimonials': testimonials,
    }
    return render(request, 'Mega Consulting-Website/about.html', context)


def blog(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = TopFooter.objects.first()
    footer_instance = Footer.objects.first()
    posts = BlogPost.objects.all()
    
   
    paginator = Paginator(posts, 3)  # Display 3 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    recent_posts = BlogPost.objects.all()

    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'posts': posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'Mega Consulting-Website/blog.html', context)


def blogSingle(request, pk):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = TopFooter.objects.first()
    footer_instance = Footer.objects.first()
    post = BlogPost.objects.get(id = pk)
    recent_posts = BlogPost.objects.all()
    tag = BlogPost.objects.get(id = pk)
   
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'post': post,
        'recent_posts': recent_posts,
        'tag': tag,
    }
    return render(request, 'Mega Consulting-Website/blog-single.html', context)


def contactUs(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = TopFooter.objects.first()
    footer_instance = Footer.objects.first()
    offices = Office.objects.all()

    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'offices': offices,
       
    }
    return render(request, 'Mega Consulting-Website/contact.html', context)



def allServices(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = audit_And_Non_Assurance_contact.objects.first()
    footer_instance = Footer.objects.first()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
       
    }
    return render(request, 'Mega Consulting-Website/services-s2.html', context)




def audit_And_Non_Assurance_Services(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = audit_And_Non_Assurance_contact.objects.first()
    footer_instance = Footer.objects.first()
    team_members = audit_And_Non_Assurance_team.objects.all()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'team_members': team_members,
    }
    return render(request, 'Mega Consulting-Website/audit_And_NonAssuranceServices.html', context)

def taxAdvisoryServices(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = taxadvisory_contact.objects.first()
    footer_instance = Footer.objects.first()
    team_members = taxadvisory_team.objects.all()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'team_members': team_members,
    }
    return render(request, 'Mega Consulting-Website/tax_Advisory_Services.html', context)

def accounting_and_finance_Services(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = accounting_and_finance_contact.objects.first()
    footer_instance = Footer.objects.first()
    team_members = accounting_and_finance_team.objects.all()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'team_members': team_members,
    }
    return render(request, 'Mega Consulting-Website/accounting_and_finance.html', context)

def business_Governance_Advisory(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = accounting_and_finance_contact.objects.first()
    footer_instance = Footer.objects.first()
    team_members = accounting_and_finance_team.objects.all()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'team_members': team_members,
    }
    return render(request, 'Mega Consulting-Website/business_Governance_Advisory.html', context)

def company_secretarial_services(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = accounting_and_finance_contact.objects.first()
    footer_instance = Footer.objects.first()
    team_members = accounting_and_finance_team.objects.all()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'team_members': team_members,
    }
    return render(request, 'Mega Consulting-Website/Company_secretarial_services.html', context)

def management_Consulting_services(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = accounting_and_finance_contact.objects.first()
    footer_instance = Footer.objects.first()
    team_members = accounting_and_finance_team.objects.all()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'team_members': team_members,
    }
    return render(request, 'Mega Consulting-Website/management_Consulting_services.html', context)

def it_Consultancy_services(request):
    navigation_bar_data = NavigationBar.objects.first()
    topfooter = accounting_and_finance_contact.objects.first()
    footer_instance = Footer.objects.first()
    team_members = accounting_and_finance_team.objects.all()
    context = {
        'navigation_bar_data': navigation_bar_data,
        'topfooter': topfooter,
        'footer_instance': footer_instance,
        'team_members': team_members,
    }
    return render(request, 'Mega Consulting-Website/IT_Consultancy_services.html', context)
