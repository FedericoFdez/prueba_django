from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from .forms import MessageForm

# Now we're using Class-based views

class FirstMessageView(FormView):
    template_name = 'simple_form/name.html'
    form_class = MessageForm
    success_url = '/simpleform/known'

    def render_to_response(self, context):
        # if there is a cookie, redirect to KnownUserView
        if 'last_message' in self.request.session:
            return HttpResponseRedirect('/simpleform/known')
        return super(FirstMessageView, self).render_to_response(context)      

    def form_valid(self, form):
        # save field in user cookie
        self.request.session['last_message'] = form.cleaned_data['message']
        return super(FirstMessageView, self).form_valid(form)

class KnownUserView(FormView):
    template_name = 'simple_form/result.html'
    form_class = MessageForm
    success_url = '/simpleform/known'

    def render_to_response(self, context):
        # if there is no cookie, redirect to FirstMessageView
        if not 'last_message' in self.request.session:
            return HttpResponseRedirect('/simpleform')
        return super(KnownUserView, self).render_to_response(context)

    def form_valid(self, form):
        # update field in user cookie
        self.request.session['last_message'] = form.cleaned_data['message']
        return super(KnownUserView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # save field in context for the template to render correctly
        context = super(KnownUserView, self).get_context_data(**kwargs)
        if 'last_message' in self.request.session:
            context['result'] = self.request.session['last_message']
        return context