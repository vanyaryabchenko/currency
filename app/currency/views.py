from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail

from currency.forms import SourceForm, RateForm, ContactUsForm
from currency.models import Rate, ContactUs, Source


# Create your views here.
class RateListView(ListView):
    template_name = 'rate_table.html'
    queryset = Rate.objects.all()


class RateCreateView(CreateView):
    template_name = 'rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')


class RateDetailView(DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()


class RateUpdateView(UpdateView):
    template_name = 'rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_table.html'


class ContactUsCreateView(CreateView):
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('currency:contactus-list')
    form_class = ContactUsForm

    def _send_mail(self):
        subject = 'Contact Us'
        message = f'''
        email_from: {self.object.email_from}
        subject: {self.object.subject}
        message: {self.object.message}
        '''
        recipient = 'support@gmail.com'

        send_mail(
            subject,
            message,
            self.object.email_from,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('currency:contactus-list')
    form_class = ContactUsForm


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_details.html'


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy('currency:contactus-list')


class SourceListView(ListView):
    template_name = 'source_table.html'
    queryset = Source.objects.all()


class SourceCreateView(CreateView):
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    template_name = 'source_update.html'
    form_class = SourceForm
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')


class SourceDeleteView(DeleteView):
    template_name = 'source_delete.html'
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')


class SourceDetailsView(DetailView):
    template_name = 'source_details.html'
    queryset = Source.objects.all()


class IndexView(TemplateView):
    template_name = 'index.html'
