from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import MessageForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's a valid:
        if form.is_valid():
            request.session['last_message'] = form.cleaned_data['message']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'simple_form/result.html', {'form': form,'result': request.session['last_message']})

    elif 'last_message' in request.session:
        form = MessageForm()
        return render(request, 'simple_form/result.html', {'form': form,'result': request.session['last_message']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MessageForm()

    return render(request, 'simple_form/name.html', {'form': form})