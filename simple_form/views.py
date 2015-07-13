from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import MessageForm

def get_message(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's a valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            request.session['last_message'] = form.cleaned_data['message']

            # render result
            return render(request, 'simple_form/result.html', {'form': MessageForm(),'result': request.session['last_message']})

    # if GET and cookie exists, render result
    elif 'last_message' in request.session:
        form = MessageForm()
        return render(request, 'simple_form/result.html', {'form': form,'result': request.session['last_message']})

    # if GET (or any other method) and no cookie we'll create a blank form
    else:
        form = MessageForm()

    return render(request, 'simple_form/name.html', {'form': form})