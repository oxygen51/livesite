from django.shortcuts import render
from .models import Category, PortfolioItem, ContactInfo, Education, WorkHistory
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views import View



from django.views.generic import TemplateView
from .models import Banner, CounterData, Service, Testimonial, PricingPlan
from django.db.models import QuerySet
import random

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = Banner.objects.first()
        context['counter_data'] = CounterData.objects.first()
        context['services'] = Service.objects.all()
        context['testimonials'] = self.get_random_testimonials()
        context['pricing_plans'] = PricingPlan.objects.all()
        return context

    def get_random_testimonials(self) -> QuerySet:
        """Fetch testimonials in a random order."""
        testimonials = list(Testimonial.objects.all())
        random.shuffle(testimonials)  # Shuffle the queryset
        return testimonials








def blog(request):
 return render(request, 'blog.html')

def publication(request):
 return render(request, 'publication.html')




class Contact(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        contact_info = ContactInfo.objects.first()
        return render(request, self.template_name, {'contact_info': contact_info})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('text')

        if not name or not email or not message:
            contact_info = ContactInfo.objects.first()
            return render(request, self.template_name, {
                'error': 'Please fill in all fields.',
                'contact_info': contact_info
            })

        subject = f"Message from {name}"
        message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        recipient_email = 'mdkalam6.1998@gmail.com'

        try:
            send_mail(
                subject,
                message_body,
                email,
                [recipient_email],
                fail_silently=False,
            )
            contact_info = ContactInfo.objects.first()
            return render(request, self.template_name, {
                'success': 'Your message has been sent successfully!',
                'contact_info': contact_info
            })

        except Exception as e:
            contact_info = ContactInfo.objects.first()
            return render(request, self.template_name, {
                'error': f"Error sending email: {str(e)}",
                'contact_info': contact_info
            })





class History(TemplateView):
    template_name = 'history.html'

    def get_context_data(self, **kwargs):
        education_data = Education.objects.all()[:4]
        work_history_data = WorkHistory.objects.all()[:4]
        
        context = super().get_context_data(**kwargs)
        context['education_data'] = education_data
        context['work_history_data'] = work_history_data
        
        return context




class Achievement(TemplateView):
    template_name = 'achievement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        all_items = PortfolioItem.objects.all()

        paginator = Paginator(all_items, 12)
        page = self.request.GET.get('page', 1)

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        current_page = page_obj.number
        total_pages = paginator.num_pages

        pagination_range = self.get_pagination_range(current_page, total_pages)

        context['page_obj'] = page_obj
        context['pagination_range'] = pagination_range

        return context

    def get_pagination_range(self, current_page, total_pages, delta=2):
        range_with_dots = []

        if total_pages <= 7 + (delta * 2):
            range_with_dots = list(range(1, total_pages + 1))
        else:
            start = max(current_page - delta, 2)
            end = min(current_page + delta, total_pages - 1)
            range_with_dots.append(1)

            if start > 2:
                range_with_dots.append("...")

            range_with_dots.extend(range(start, end + 1))

            if end < total_pages - 1:
                range_with_dots.append("...")

            range_with_dots.append(total_pages)

        return range_with_dots






def project(request):
 return render(request, 'project.html')