from django.http import Http404
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Subscription


class ConfirmSignupView(TemplateView):
    """
    Confirm the user's email address
    when they click on the link in the email from newsletter (homepage)
    """
    template_name = 'signup_confirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        confirmation_token = kwargs.get('confirmation_token')

        try:
            subscription = Subscription.objects.get(
                confirmation_token=confirmation_token)
            subscription.is_verified = True
            # set the confirmed_at date
            subscription.confirmed_at = timezone.now()
            # remove the uuid so the user can't use the link again
            subscription.confirmation_token = None
            subscription.save()
            full_name = f'{subscription.first_name} {subscription.last_name}'
            context.update({
                'full_name': full_name,
                'email': subscription.email
            })

        except Subscription.DoesNotExist:
            raise Http404

        return context
