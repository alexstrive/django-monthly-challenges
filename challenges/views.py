import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

challenges = {
    "january": 'hello world',
    "february": "for feb",
    "march": "for march"
}


def index(request):
    return render(request, "index.challenges.html", {
        "months": challenges.keys()
    })


# Create your views here.
def monthly_challenge(request, month):
    challenge_text = challenges.get(month) or "not supported"
    return render(request, "challenge.challenges.html", {
        "month": month,
        "challenge_text": challenge_text
    })


def monthly_challenge_num(request, month):
    selected_month = list(challenges.keys())[month + 1]
    redirect_path = reverse('month_by_name', args=[selected_month])
    return HttpResponseRedirect(redirect_path)
