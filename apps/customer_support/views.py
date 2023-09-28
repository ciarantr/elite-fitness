from django.views.generic import TemplateView


class AboutView(TemplateView):
    """
    This view handles the display of the about page
    """
    template_name = 'about.html'
    title = 'About Us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
