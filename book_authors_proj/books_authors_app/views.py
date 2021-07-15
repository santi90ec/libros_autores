from django.shortcuts import redirect, render,HttpResponse
from .models import Book , Author
# Create your views here.
def index(request):
    if request.method=="GET":
        books=Book.objects.all()
        return render(request,'index.html',{'all':books})
def addBook(request):
    if request.method=="POST":
        newbook=Book.objects.create(title=request.POST['titulo'],desc=request.POST['descripcion'])
        return redirect("/")
def book(request,number):
    if request.method=="GET":
        book=Book.objects.get(id=number)
        bookAut = Author.objects.filter(books=book)
        
        context={
            'libro':  book,
            'autores': bookAut
        }
        return render(request,'book.html',context)
def indexAuthor(request):
    if request.method=="GET":
        autores=Author.objects.all()
        return render(request,'indexAuthor.html',{'authorObj':autores})
    
def addAuthor(request):
    return HttpResponse("Hola")
