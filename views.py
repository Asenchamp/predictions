from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Match, Choice, League
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('betpolls:index')

    if request.method == 'POST':
        email = request.POST.get('email')  # Get email address
        password = request.POST.get('password')

        # Check if email exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Email or password do not match.')
            return render(request, 'login_registration.html', {'page': page})

        # Authenticate the user
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect('betpolls:index')
        else:
            messages.error(request, 'Email or password do not match.')

    return render(request, 'login_registration.html', {'page': page})

def logoutUser(request):
  logout(request)
  return redirect('betpolls:index')

from .forms import UserRegistrationForm

def registerPage(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('betpolls:index')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'login_registration.html', {'form': form})



# Get questions and display those questions
def index(request):
    leagues = League.objects.all()
    latest_match_list = Match.objects.order_by('-match_date')[:5]
    context = {'latest_match_list': latest_match_list,
               'leagues': leagues
               }
    return render(request, 'index.html', context)

# Show match and choices
def detail(request, match_id):
    try:
        match = Match.objects.get(pk = match_id)
    except Match.DoesNotExist:
        raise Http404('Match does not exist')
    return render(request, 'detail.html', 
                    {'match': match,
                 })
 
#Get match and display results
def results(request, match_id):
    match = get_object_or_404(Match, pk = match_id)
    return render(request, 'results.html',                  
                    {'match':match})


# Vote for a match choice
@login_required
def vote(request, match_id):
    match = get_object_or_404(Match, pk=match_id)

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('betpolls:login'))

    # Check if the user has already voted for any choice in this match
    if Choice.objects.filter(match=match, voter=request.user).exists():
        return render(request, 'detail.html', {
            'match': match,
            'error_message': 'You already selected a choice for this match.'
        })
    try:
        selected_choice = match.choice_set.get(pk=request.POST['card'])   
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'match': match,
            'error_message': 'You did not select a choice.'
        })
    else:
        selected_choice.votes += 1
        selected_choice.voter = request.user
        selected_choice.save()
        return HttpResponseRedirect(reverse('betpolls:results', args=(match.id,)))

def get_matches(request, league_id):
    leagues = League.objects.all()
    latest_match_list = Match.objects.filter(league_id=league_id)
    context = {'latest_match_list': latest_match_list,
               'leagues': leagues
               }
    return render(request, 'index.html', context)

    
"""

# Get questions and display those questions
def index(request):
    latest_match_list = Match.objects.order_by('-match_date')[:5]
    context = {'latest_match_list': latest_match_list}
    return render(request, 'index.html', context)

# Show match and choices
def detail(request, match_id):
    try:
        match = Match.objects.get(pk = match_id)
    except Match.DoesNotExist:
        raise Http404('Match does not exist')
    return render(request, 'detail.html', 
                    {'match': match})

#Get match and display results
def results(request, match_id):
    match = get_object_or_404(Match, pk = match_id)
    return render(request, 'results.html',                  
                    {'match':match})


# Vote for a match choice
@login_required
def vote(request, match_id):
    match = get_object_or_404(Match, pk=match_id)

    # Check if the user has already voted for any choice in this match
    if Choice.objects.filter(match=match, voter=request.user).exists():
        return render(request, 'detail.html', {
            'match': match,
            'error_message': 'You have already voted for a choice in this match.'
        })

    try:
        selected_choice = match.choice_set.get(pk=request.POST['choice'])   
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'match': match,
            'error_message': 'You did not select a choice.'
        })
    else:
        selected_choice.votes += 1
        selected_choice.voter = request.user
        selected_choice.save()
        return HttpResponseRedirect(reverse('betpolls:results', args=(match.id,)))
"""




"""
def vote(request, match_id):
    match = get_object_or_404(Match, pk = match_id)
    try:
        selected_choice = match.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', 
                      { 'match': match,
                        'error_message': 'You did not select a choice.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('betpolls:results', args = (match.id,)))
    
"""



# Create your views here.
""""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import Http404

from .models import Question, Choice

# Get questions and display those questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', 
                    {'question': question})

#Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html',                  
                    {'question':question})

# Vote for a qerstion choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', 
                      { 'question': question,
                        'error_message': 'You did not select a choice.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
"""