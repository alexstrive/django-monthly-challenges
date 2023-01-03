import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

challenges = {
    "january": 'hello world',
    "february": "for feb",
    "march": "for march"
}


def index(request):
    challenges_html = "".join(map(
        lambda challenge: f"""<li><a href="/challenges/{challenge}">{challenge}</a></li>""", list(challenges.keys())))

    resp = f"""
      <ul>
        {challenges_html}
      </ul>
    """
    return HttpResponse(resp)


# Create your views here.
def monthly_challenge(request, month):
    challenge_text = challenges.get(month) or "not supported"
    formatted_text = f"<h1>{challenge_text}</h1>"
    return HttpResponse(formatted_text)


def monthly_challenge_num(request, month):
    selected_month = list(challenges.keys())[month + 1]
    redirect_path = reverse('month_by_name', args=[selected_month])
    return HttpResponseRedirect(redirect_path)
