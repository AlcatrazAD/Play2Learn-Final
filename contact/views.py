import html

from django.urls import reverse_lazy

from django.views.generic import FormView, TemplateView

from users.emails.email import send_email
from .forms import ContactForm


class ContactView(FormView):
    template_name = 'contact/contacted.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')
    
    def form_valid(self, form):
        data = form.cleaned_data
        to = 'ziiondrianrose@gmail.com'
        subject = 'a summons request'
        content = f'''<p>Hey bestie!</p>
            <p>they're trying to find you:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)


class ContactThanksView(TemplateView):
    template_name = 'contact/thanks.html'
