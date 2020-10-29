from django.shortcuts import render, HttpResponse, redirect
# from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views import generic
from .models import *
import bcrypt





def index(request):


    return render(request, "BookReview/index.html")


def successregistration(request):

    
        if len(User.objects.filter(email = request.POST['email'])) > 0:
            context = {
                "email_messages" : request.POST['email'] + ' : email already exists'
            }
            return render(request, 'BookReview/index.html', context)
      
        password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        user = User(name= request.POST['name'], alias = request.POST['alias'], email= request.POST['email'], password_hash = password_hash)
        user.save()

        user_method= request.POST['user_method']


        return redirect("/success/" , user_method)


def success(request):

    request.session.delete()

  
    return render(request, 'BookReview/index.html')



def successlogin(request):

    if request.method == "POST":
        user = User.objects.get(email=request.POST['lemail'])

        # Check passwords to see if they match
    if bcrypt.checkpw(request.POST['password'].encode(), user.password_hash.encode()):
        print("password match")
    else:
        print("failed password")     

    if 'alias' not in request.session:
        request.session['alias'] = user.alias
    if 'id' not in request.session:
        request.session['id'] = user.id     
    if 'email' not in request.session:
        request.session['lemail'] = user.email 

  

        
    
        print(request.session['alias'])

    return redirect('/login/')

def login(request):

    if 'alias' not in request.session:
        request.session['alias'] = user.alias
    # if 'user_id' not in request.session:
    #     request.session['user_id'] = user.user_id
    if 'id' not in request.session:
        request.session['id'] = user.id

    email = request.session["lemail"]
    user = User.objects.get(email=email)
    books =  Book.objects.order_by("title")
    mybookreviews = Review.objects.order_by("-created_at")[:3]    

    context = {
        "email" : user.email,
        "alias" : user.alias,
        "user_review" : user.userreviews,
        "books" : books,
        "mybookreview" : mybookreviews,
    }

    return render(request, "BookReview/bookshome.html", context)

def loadaddreview(request):
  
    
    authors = Book.objects.values('author').distinct()

    context = {
        "authors" : authors
        
    }

    return render(request, 'BookReview/addbookreview.html', context)

def addbookreview(request):

    if request.method == "POST":

        this_user = User.objects.get(email=request.session['lemail'])

        bookcreate = Book.objects.create(title = request.POST['booktitle'], author = request.POST['author'], submitted_by = this_user)

        books_review = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], user_review = this_user, books_review = bookcreate)

       

    return redirect('/addreview/')

    # --------------showing 1 book review----------- 

def bookreview(request, id):

    mybookreview = Book.objects.get(id=id)
    the_user = User.objects.get(email = request.session['lemail'])

    context = {
        "mybookreview" : mybookreview,
        "reviews": Review.objects.filter(books_review=mybookreview).order_by("-created_at"),
        "the_user" : the_user,

    }

    return render (request, 'BookReview/bookreview.html', context)


def addreview(request, id):

    if request.method == "POST":
        review = request.POST['review']
        rating = request.POST['rating']
        user_review = User.objects.get(email = request.session['lemail'])
        this_book = Book.objects.get(id = id)

        print(this_book)

        Review.objects.create(review = review, rating = rating, books_review = Book.objects.get(id = id), user_review = user_review)

    return redirect('/bookreview/' + id + '/')

def userreview(request, id):

    mybookreview = Book.objects.get(id=id)
    the_user = User.objects.get(email = request.session['lemail'])
    reviews = Review.objects.filter(books_review=mybookreview).count()
    reviewed_books = Review.objects.filter(user_review = id).order_by("-created_at")

    context = {
        "mybookreview" : mybookreview,
        "reviews": reviews,
        "the_user" : the_user,
        "reviewed_books" : reviewed_books

    }

    return render (request, 'BookReview/userreview.html', context)



def delete_review(request, id):

    review = Review.objects.get(id=id)
    review.delete()

    return redirect('/bookreview/')



# --------------------------logout--------------------------- 


def logout(request):
    request.session.delete()
    print('session cleared')
    return redirect('/')
