from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def get_data(query):
    query=query.replace(' ','+')
    URL = "https://www.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q="+query
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    lol=soup.findAll('div',attrs = {'class':'PartialSearchResults-item'})
    ans=[]
    for _ in lol:
        data={}
        data['title']=_.find('a',attrs={'class':'PartialSearchResults-item-title-link result-link'}).text
        data['abstract']=_.find('p',attrs = {'class':'PartialSearchResults-item-abstract'}).text
        data['link']="https://"+_.find('p',attrs = {'class':'PartialSearchResults-item-url'}).text
        ans.append(data)
    return ans

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
    if(request.method=="POST"):
        query = request.POST["search"]
        data = get_data(query)
        return render(request,'search.html',{'final_result' : data})
    else:
        return render(request,'search.html')
