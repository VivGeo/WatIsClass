from django.template import loader
from .models import Room
# noinspection PyPep8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# noinspection PyPep8
import random, string
# noinspection PyPep8
from .forms import CourseForm, RoomForm


# noinspection PyPep8,PyPep8
def index(request):
    template = loader.get_template('openroom/index.html')
    return HttpResponse(template.render(request))


# noinspection PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8
@csrf_exempt
def generate(request):
    # if this is a POST request we need to process the form data
    # noinspection PyPep8,PyPep8,PyPep8,PyPep8,PyPep8
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CourseForm(request.POST)
        # check whether it's valid:
        # noinspection PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8
        if form.is_valid():
            room_code = ''
            # noinspection PyPep8,PyPep8
            for x in range(0, 10):
                room_code += random.choice(string.ascii_letters)
            room = Room(lectures=form.cleaned_data['num_lectures'],name=form.cleaned_data['course'],code=room_code)
            # noinspection PyPep8
            room.code = room_code;
            # noinspection PyPep8
            room.save();
            return HttpResponse('You can visit your room at ' + room_code)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CourseForm()

    return render(request, 'openroom/index.html', {'form': form})
