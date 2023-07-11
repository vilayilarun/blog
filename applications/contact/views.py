import json

from django.views import generic
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse

from .forms import ContactForm


class ContactView(generic.FormView):

    form_class = ContactForm
    template_name = "contact/contact_page.html"

    def form_valid(self, form):
        text_template = get_template('email_templates/contact_message.html')
        user_name = form.cleaned_data['first_name'] + form.cleaned_data['last_name']
        subject = 'Contact request from {}'.format(user_name)
        context = {'formentry': self.request.POST}
        text_content = text_template.render(context)
        from_email = settings.EMAIL_HOST_USER
        to = [settings.EMIAL_HOST_ADMIN]
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(text_content, "text/html")
        msg.send()
        form.save()
        return JsonResponse({'status':'success'})

    def form_invalid(self, form):
        return HttpResponse(json.dumps({'result': {'status': 'form_error', 'errors': form.errors}}),
                            content_type='application/json')

    def get_success_url(self):
        return '/'
