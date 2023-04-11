
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from currency.filters import RateFilter, SourceFilter, ContactUsFilter
from currency.forms import SourceForm, RateForm, ContactUsForm
from currency.models import Rate, ContactUs, Source


# Create your views here.
class RateListView(FilterView):
    template_name = 'rate_table.html'
    queryset = Rate.objects.all().select_related('source')
    paginate_by = 10
    filterset_class = RateFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


class RateCreateView(CreateView):
    template_name = 'rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')


class RateDetailView(LoginRequiredMixin, DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()


class RateUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsListView(FilterView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_table.html'
    paginate_by = 10
    filterset_class = ContactUsFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


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

        from currency.tasks import send_mail
        send_mail.delay(subject, message)

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


class SourceListView(FilterView):
    template_name = 'source_table.html'
    queryset = Source.objects.all()
    paginate_by = 10
    filterset_class = SourceFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'
        )
        return context


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
