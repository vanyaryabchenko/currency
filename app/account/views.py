
from django.contrib.auth import get_user_model

from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView


from account.forms import UserSignUpForm


class UserSignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_user_model().objects.filter(username=username).first()
        if user is not None:
            user.is_active = True
            user.save(updated_fields=['is_active'])
        url = super().get_redirect_url(*args, **kwargs)
        return url


