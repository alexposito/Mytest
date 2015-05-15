# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.template import RequestContext
from filmak.models import filma, bozkatzailea
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@login_required(login_url='/')
def hasiera(request):
    erabiltzailea = request.user
    return render_to_response('filmak/hasiera.html', {'user':erabiltzailea}, context_instance=RequestContext(request))

@login_required(login_url='/')
def ikusi(request):
    filmak = filma.objects.all()
    return render_to_response('filmak/ikusi.html', {'filmak':filmak}, context_instance=RequestContext(request))

@login_required(login_url='/')
def bozkatu(request):
    erabiltzailea = request.user
    return render_to_response('filmak/hasiera.html', {'user':erabiltzailea}, context_instance=RequestContext(request))

@login_required(login_url='/')
def bozkak(request, filmId):
    film = filma.objects.get(pk=filmId)
    bozkatzaileak = film.bozkatzailea_set.all()
    return render_to_response('filmak/bozkak.html', {'filma':filma, 'bozkatzaileak':bozkatzaileak}, context_instance=RequestContext(request))


@receiver(post_save, sender=User)
def bozkatzailea_sortu(sender, instance, created, **kwargs):
    if created:
        bozka = bozkatzailea(erabiltzailea_id=instance)
        bozka.save()

#def detail(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
#    return render_to_response('polls/detail.html', {'poll': p},
#                               context_instance=RequestContext(request))

#def results(request, poll_id):
#    return HttpResponse("You're looking at the results of poll %s." % poll_id)

#def vote(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
#    try:
#        selected_choice = p.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
#        return render_to_response('polls/detail.html', {
#            'poll': p,
#            'error_message': "You didn't select a choice.",
#        }, context_instance=RequestContext(request))
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
