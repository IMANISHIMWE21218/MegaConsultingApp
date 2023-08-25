from django.db import models

# Create your models here.

class Topbar(models.Model):
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)
    vimeo_link = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    opening_time = models.CharField(max_length=35, blank=True, null=True)
    

    def __str__(self):
        return "Topbar Links and email  Configuration"

class NavigationBar(models.Model):
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    mobile_contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return "Navigation Bar Configuration"
    


class ImageSlider(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='sliderImage/', blank=False)
    

    def __str__(self):
        return self.title
    


class SlideDashboardSection(models.Model):
    ICON_CHOICES = [
        ('ti-user', 'User Icon'),
        ('flaticon-trophy', 'Trophy Icon'),
        ('flaticon-leadership', 'Leadership Icon'),
        # Add more icon choices as needed
    ]

    count = models.CharField(max_length=9, help_text='The count number (e.g., "01.", "02.")', blank=False)
    text = models.CharField(max_length=30, help_text='The section title', blank=False)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, help_text='The icon class name')

    def __str__(self):
        return f"{self.count} {self.text}"
    

class WhyYouUsFeature_Home(models.Model):
    ICON_CHOICES = [
        ('flaticon-network-1', 'Network Icon 1'),
        ('flaticon-circular-label-with-certified-stamp', 'certified-stamp'),
        ('flaticon-chip', 'chip'),
        ('flaticon-24-hours', 'flaticon-24-hours'),
    ]

    # top_message = models.CharField(max_length=250)
    icon = models.CharField(max_length=100, choices=ICON_CHOICES, help_text='Select an icon (e.g.,"flaticon-24-hours")')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    aboutUsTitle = models.CharField(max_length=100)
    youtube_video_id = models.CharField(max_length=100, help_text='Youtube video code (e.g.,"httyAiqojjo")')
    aboutUsDescription = models.TextField()
    sideImage = models.ImageField(upload_to='about_us_banners/')
    ourMission = models.TextField()
    ourVision = models.TextField()
    employedMembers = models.CharField(max_length=9)
    completedTasks = models.CharField(max_length=12)
    awardworn =models.CharField(max_length=10)

    def __str__(self):
        return self.aboutUsTitle
    
   # The top footer is the above home page footer banner with contact and description 
class TopFooter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.title

class audit_And_Non_Assurance_contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()
    
class taxadvisory_contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()

class accounting_and_finance_contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()

class business_Governance_contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()

class company_secretarial_contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()


class management_Consulting_contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()

class IT_Consultancy_contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()

    
class Footer(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    office_time = models.CharField(max_length=15, help_text='office time  (e.g.,"10AM - 17PM")')

    footer_description = models.TextField()
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    pinterest_link = models.URLField(blank=True)
    video_link = models.URLField(blank=True)

    def __str__(self):
        return self.address

class PartnerAndBrands(models.Model):
    image = models.ImageField(upload_to='partners/')  # This assumes you have installed and configured Django's ImageField correctly

    def __str__(self):
        return f"PartnerAndBrands image {self.id}"
    
# the general team model for home page and about us page 
class OurTeam_AboutUs(models.Model):
    memberImage = models.ImageField(upload_to='team/')
    memberName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.memberName

from django.db import models


# different services and their team models 

class audit_And_Non_Assurance_team(models.Model):
    memberImage = models.ImageField(upload_to='team/')
    memberName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.memberName

class taxadvisory_team(models.Model):
    memberImage = models.ImageField(upload_to='team/')
    memberName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.memberName

class accounting_and_finance_team(models.Model):
    memberImage = models.ImageField(upload_to='team/')
    memberName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.memberName

class business_Governance_team(models.Model):
    memberImage = models.ImageField(upload_to='team/')
    memberName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.memberName

class company_secretarial_team(models.Model):
    memberImage = models.ImageField(upload_to='team/')
    memberName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.memberName

class management_Consulting_team(models.Model):
    memberImage = models.ImageField(upload_to='team/')
    memberName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.memberName

class IT_Consultancy_team(models.Model):
    memberImage = models.ImageField(upload_to='team/')
    memberName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.memberName
    





class Testimonial(models.Model):
    quote = models.TextField()
    client_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.client_name
    
    
class Office(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
# class BlogPost(models.Model):
#     author = models.CharField(max_length=100, blank=True, null=True)
#     date = models.DateField()
#     category = models.CharField(max_length=100)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = models.ImageField(upload_to='blog_images/')
#     alt_text = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.title


class BlogPost(models.Model):
    author = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    blog_picture = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    alt_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title






