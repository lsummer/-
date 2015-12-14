from django.http import HttpResponse, HttpResponseRedirect
from webapp.models import Users,Salary,People,Full_salary,Yewu
from django.contrib import auth
import datetime
username = ""
global username

from django.template import Context
from django.shortcuts import render_to_response

def main(request):
    return render_to_response('main.html')
def inset_people(request): 
    global username
    if request.POST:
        global username
        user = Users.objects.get(username = username)
        post = request.POST
        new_people = People(
            username1_id = user.id,
            name = post["name"],
            nation = post["nation"],
            phone = post["phone"],
            email = post["email"],
            date = post["date"],
            address = post["address"],
            postkey_id = Salary.objects.get(post_name=post["post_name"]).id,
            birthday = post["birthday"]
            )
        if post["sex"] == "M":       
            new_people.sex = True
        else:
            new_people.sex = False       
        new_people.save()
    return render_to_response("insert_people.html")

def insert_yewu(request):
    global username
    if request.POST:
        global username
        user = Users.objects.get(username = username)
        post = request.POST
        new_yewu = Yewu(
            username1_id = user.id,
            title = post["title"],
            client = post["client"],
            phone = post["phone"],
            money = post["money"],
            person = post["person"],
            date = post["date"],
            beizhu = post["beizhu"],
            checkinDate = datetime.datetime.now()
            )
        if post["zhishou"] == "S":       
            new_yewu.zhishou = True
        else:
            new_yewu.zhishou = False       
        new_yewu.save()
    return render_to_response("insert_yewu.html")

def browse_yewu(request):
    global username
    user = Users.objects.get(username = username)
    yewu_list = Yewu.objects.filter(username1_id = user.id)
    c = Context({"yewu_list":yewu_list})
    return render_to_response("show_yewu.html", c) 
    
def people_salary_browse(request):
    people = People.objects.get(id=request.GET["id"])
    salary=Full_salary.objects.filter(peopleid=request.GET["id"])
    c = Context({"people":people, "salary":salary})
    return render_to_response("show_salary.html", c)
        
    
def browse_people(request):
    global username
    user = Users.objects.get(username = username)
    people_list = People.objects.filter(username1_id = user.id)
    c = Context({"people_list":people_list})
    return render_to_response("show_people.html", c)  

def search(request):
    if 'search_name' in request.GET and People.objects.get(name=request.GET['search_name']):
        people= People.objects.get(name=request.GET['search_name'])
        postss = Salary.objects.get(id=people.postkey_id)
        salary = Full_salary.objects.filter(peopleid_id=people.postkey_id)
        if request.POST:
            post = request.POST
            new_salary = Full_salary(
                peopleid_id = people.id,
                datemonth = post["date1"],
                tsavings = post["tsaving"],             
                zsavings = post["zsaving"]
                )
            new_salary.base = Salary.objects.get(id=people.postkey_id).base
            new_salary.all_salary = new_salary.base+ (float)(post["tsaving"])+(float)(post["zsaving"])
            new_salary.save()
            return render_to_response('main.html')
        return render_to_response('show_salary.html', {'people':people,'salary':salary,'salaryen':postss})
    else:
        return HttpResponse('please submit a seach term')
'''
def delete(request): 
    get_id = request.GET["id"]
    People.objects.get(id=get_id).delete()
    People.objects.all()
    return render_to_response("delete.html")
    return render_to_response("addr_book.html")
'''        
def details_yewu(request):
    if 'search_name' in request.GET and Yewu.objects.get(title=request.GET['search_name']):
        yewu= Yewu.objects.get(title=request.GET['search_name'])
        global username
        user = Users.objects.get(username = username)
        yewu_list = Yewu.objects.filter(username1_id = user.id)
        if yewu.username1_id == user.id:
            return render_to_response('YEWUfull.html', {'yewu':yewu})
    return render_to_response('show_yewu.html', {"yewu_list":yewu_list})
        
def update(request): 
    if 'search_name' in request.GET and People.objects.get(name=request.GET['search_name']):
        people= People.objects.get(name=request.GET['search_name'])  
        postss = Salary.objects.get(id=people.postkey_id)
        if request.POST:
            post = request.POST
            if post["nation"]!="":
                people.nation = post["nation"]
            if post["phone"]!="":
                people.phone = post["phone"],
            if post["email"]!="":
                people.email = post["email"],
            if post["date"]!="":
                people.date = post["date"],
            if post["address"]!="":            
                people.address = post["address"],
            if post["post_name"]!="":            
                people.postkey_id = Salary.objects.get(post_name=post["post_name"]).id,
            if post["birthday"]!="":            
                people.birthday = post["birthday"]
            people.save()
            return render_to_response('main.html')
        return render_to_response('update.html', {'people':people,'post':postss})

def update_search(request):
    return render_to_response('update_search.html')
    
def login(request):
    global username
    if request.POST:
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        p = Users.objects.filter(username = username)
        if p:
            p=p[0]
            if password == p.password:
                return render_to_response("main.html")
        else:
            return HttpResponseRedirect("/login_error/")
    return render_to_response("login.html")  
    
def register(request):
    if "username" in request.GET:
        password1 = request.GET["password"]
        passwordco = request.GET["password1"]
        if(password1==passwordco):
            user = Users(
                username = request.GET["username"],
                password = request.GET["password"]
            )
            user.save()
            return HttpResponseRedirect("/login/")
    return render_to_response("register.html")
    
def login_error(request):
    return render_to_response("login_error.html")
    
def logout(request):
    auth.logout(request)
    return render_to_response("/login/")
