from django.http import JsonResponse
import json
from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.http import HttpRequest
from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact,customerscore,surveyscore,accountids, balances
from .serializers import ContactSerializer,CustSerializer,SurveySerializer

# Create your views here.

# For Fetching the balances from CMA9 Account API and find if the customer needs a debt buddy.
def memos(request):

    custo = request.POST['Cust']
    username = request.POST['Cust'] + '@alphainterface.org'

# 1 - Retrieving access token

    url = "https://ob.rbs.useinfinite.io/token"
    client_id = 'j9eZlvNwP10ir0Vs1dEX8WdM4ocXBq6X-VRKqxlGRwY'   #without = at the end
    client_secret='YJfAQnZLHl0-dhZiesY6xJ8kgNyefmeR6BD5GFOlF_Y' #without = at the end
    payload = 'grant_type=client_credentials&client_id='+client_id+'%3D&client_secret=' +client_secret+'%3D&scope=accounts'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()

    ACCESS_TOKEN = response['access_token']

#2 - Posting Account request
    url1 = "https://ob.rbs.useinfinite.io/open-banking/v2.0/account-requests"

    payload = "{\n  \"Data\": {\n    \"Permissions\": [\n      \"ReadAccountsDetail\",\n      \"ReadBalances\",\n      \"ReadTransactionsCredits\",\n      \"ReadTransactionsDebits\",\n      \"ReadTransactionsDetail\"\n    ]\n  },\n  \"Risk\": {}\n}"
    bearer1 = 'Bearer ' + ACCESS_TOKEN
    #return HttpResponse(bearer1)
    headers = {
        'Authorization': bearer1,
        'Content-Type': 'application/json',
        'x-fapi-financial-id': '0015800000jfwB4AAI'
    }

    response1 = requests.request("POST", url1, headers=headers, data=payload, verify=False).json()
    AccountRequestid_prev = response1['Data']
    AccountRequestid = AccountRequestid_prev['AccountRequestId']
    #return render(request, 'memos.html',{'name': AccountRequestid})

#3 - Approve Consent Programatically

    baseurl = "https://api.rbs.useinfinite.io/authorize?client_id="
    redi_api = 'http://localhost:8000/redirect_apis'
    redilen = len(redi_api)
    url2 = baseurl + client_id + '=&response_type=code id_token&scope=openid accounts&redirect_uri='+redi_api+'&state=ABC&request='+AccountRequestid+'&authorization_mode=AUTO_POSTMAN&authorization_username='+username
    #return HttpResponse(url)
    payload = {}
    headers= {}

    response2 = requests.request("GET", url2, headers=headers, data = payload,verify=False).json()
    au_cd = response2['redirectUri']
    AUTHORIZATION_CODE = au_cd[redilen+6:redilen+42]

    #return render(request, 'memos.html',{'name': response2, 'au' : AUTHORIZATION_CODE})

#4 - Exchange code for access token
    redi_api1 = 'http%3A//localhost%3A8000/redirect_apis'
    payload = 'client_id='+client_id+'%3D&client_secret=' +client_secret+'%3D&redirect_uri='+redi_api1+'&grant_type=authorization_code&code='+AUTHORIZATION_CODE
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response3 = requests.request("POST", url, headers=headers, data = payload,verify=False)
    try:
        response3.raise_for_status()
    except requests.exceptions.HTTPError:
        return render(request, 'about.html', {'name1': 'The Customer Number does not exist, please reenter'})
    response3 = response3.json()
    #    return render(request, 'about.html',{'name': 'The Customer Number does not exist'})
    ACCESS_TOKEN1 = response3['access_token']

#5 List the accounts
    url3 = "https://ob.rbs.useinfinite.io/open-banking/v2.0/accounts"
    payload = {}
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN1,'x-fapi-financial-id': '0015800000jfwB4AAI'}
    response4 = requests.request("GET", url3, headers=headers, data = payload,verify=False).json()
    #return render(request, 'memos.html',{'name': response4})

    a1 = response4['Data']
    a2 = a1['Account'][0]['AccountId']  #for Account id

    i = 0

    aid = []
    bid = []
    for each in a1['Account']:

        m1 = accountids()
        m1.descname = a1['Account'][i]['Description']
        m1.curr = a1['Account'][i]['Currency']
        m1.acttyp = a1['Account'][i]['AccountType']
        m1.actsubtyp = a1['Account'][i]['AccountSubType']
        m1.accountids = a1['Account'][i]['AccountId']
        j = 0
        for each1 in a1['Account'][i]['Account']:
            m1.actid = a1['Account'][i]['Account'][j]['Identification']  #for Account ids
            m1.schname = a1['Account'][i]['Account'][j]['SchemeName']  #for Scheme Name
            m1.actname = a1['Account'][i]['Account'][j]['Name']  #for Name of the account
            j += 1
            aid.append(m1)
        i += 1
#6 List the transactions for the first account id in the prototype to know elligibility for debt budy, can extend to all the account ids in the original solution
    url4 = "https://ob.rbs.useinfinite.io/open-banking/v2.0/accounts/" + a2 + '/transactions'
    payload = {}
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN1, 'x-fapi-financial-id': '0015800000jfwB4AAI'}
    response5 = requests.request("GET", url4, headers=headers, data=payload, verify=False).json()
    closingbalance = float(response5['Data']['Transaction'][-1]['Balance']['Amount']['Amount'])
    initialbalance = float(response5['Data']['Transaction'][0]['Balance']['Amount']['Amount'])
    if closingbalance - initialbalance >= 0:
        a1 = 'You have healthy account, want to enroll to Debt Buddy Programme?'
        b1 = 1      # Flag for healthy account

    else:
        a1 ='Elligible for Debt Buddy programme, submit to enroll to Debt Buddy Programme'
        b1 = 0       # Flag for the elligibility to Debt Buddy programme

    cstscor = b1
    csscr = customerscore(customernumber=custo,cstscor=cstscor)
    csscr.save()

    n1 = response5['Data']
    k = 0

    for each in n1['Transaction']:
        m1 = balances()
        m1.balactid = n1['Transaction'][k]['AccountId']
        m1.cdamount = float(n1['Transaction'][k]['Amount']['Amount'])
        m1.cdcurrency = n1['Transaction'][k]['Amount']['Currency']
        m1.cdindicator = n1['Transaction'][k]['CreditDebitIndicator']
        m1.bdtime = n1['Transaction'][k]['BookingDateTime']
        m1.balamt = float(n1['Transaction'][k]['Balance']['Amount']['Amount'])

        bid.append(m1)
        k += 1

    return render(request, 'memos.html',{'name': a1,'name1': aid, 'name2':bid})

# WellnessProvider (New API): Fetching data in JSON response
class contlist(APIView):
    def get(self,request):
        contact1 = Contact.objects.all()
        serializer = ContactSerializer(contact1, many=True)
        return Response(serializer.data)
        pass
    def post(self):
        pass

# Credit Score API: Fetching data in JSON response
class custlist(APIView):
    def get(self,request):
        cust1 = customerscore.objects.all()
        serializer = CustSerializer(cust1, many=True)
        return Response(serializer.data)
        pass
    def post(self):
        pass

# For Home page - index.html
def home(request):
    return render(request, 'index.html')

# For entering the Customer Number and hitting submit to go to the next page
def about(request):
    return render(request, 'about.html')

# For Wellness Support - Medicinal needs
def contact(request):
    if request.method == "POST":
        name  = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,address=address,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

# For Wellness Survey
def surveys(request):
    if request.method == "POST":
        scorenet = 0
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        major = request.POST.get('major')
        accounts = request.POST.get('accounts')
        if rating == 'Completely':
            scorenet +=5
        elif rating == 'Very well':
            scorenet += 4
        elif rating == 'Somewhat':
            scorenet +=3
        elif rating == 'Very little':
            scorenet +=2
        else:
            scorenet +=1

        if major == 'Completely':
            scorenet += 5
        elif major == 'Very well':
            scorenet += 4
        elif major == 'Somewhat':
            scorenet += 3
        elif major == 'Very little':
            scorenet += 2
        else:
            scorenet += 1

        if accounts == 'Always':
            scorenet += 5
        elif accounts == 'Often':
            scorenet += 4
        elif accounts == 'Sometimes':
            scorenet += 3
        elif accounts == 'Rarely':
            scorenet += 2
        else:
            scorenet += 1

        surv = surveyscore(name=name,email=email,scores=scorenet)
        surv.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'surveys.html')

# Wellness Survey API: Fetching data in JSON response
class surveylist(APIView):
    def get(self,request):
        surv1 = surveyscore.objects.all()
        serializer = SurveySerializer(surv1, many=True)
        return Response(serializer.data)
        pass

    def post(self):
        pass

def dbuddy(request):
    return render(request, 'dbuddy.html')

def surveys1(request):
    list1 = []

    return render(request, 'surveys1.html')