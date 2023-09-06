from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

monthly_challenges={
    'january':'jogg',
    'february':'sing',
    'march':'dance',
    'april':'read',
    'may':'ride',
    'june':'eat',
    'july':'drink',
    'august':'walk',
    'september':'do something',
    'october':'play',
    'november':'jump',
    'december':'the end'
    }

def index(request):
    list_items=""
    months_list=list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month=month.capitalize()
    #     month_path=reverse("month-challenge",args=[month])
    #     list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    # response_data=f"<ul>{list_items}</ul>"
    return render(request,"challenges/index.html",{ "months":months_list})





def monthly_challenge(request,month):
    

    try:
        # print(monthly_challenge[month])
        challenges=monthly_challenges[month]
        # challenges=render_to_string('challenges/challenge.html')
        return render(request,"challenges/challenge.html",{
            "text":challenges,
            "month":month
        })
    except:
        return HttpResponseNotFound('we are still not updated')
    
    
def monthly_challenge_by_number(request,month):
    monthlist=list(monthly_challenges.keys()) 
    if month>len(monthlist):
        return HttpResponseNotFound("Invalid month")
    redirect_month=monthlist[month-1]
    redirect_path=reverse('month-challenge',args=[redirect_month])

    return HttpResponseRedirect(redirect_path)

