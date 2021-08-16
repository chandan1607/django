from travello.models import destination
from django.shortcuts import render

# Create your views here.

def index(request):
    
    dest1 = destination()
    dest1.name="Bangalore"
    dest1.des="City wakes up at 4 AM "
    dest1.price=850
    dest1.image = 'destination_1.jpg'
    dest1.offer = True

    dest2 = destination()
    dest2.name="Mysore"
    dest2.des = " palace city"
    dest2.price=" 100"
    dest2.image='destination_2.jpg'

    dest3 = destination()
    dest3.name="Chikkamagalore"
    dest3.des = "The land of coffee"
    dest3.price = 1200
    dest3.image='destination_3.jpg'

    dest4 = destination()
    dest4.name="Hassan"
    dest4.des = "The land of coffee"
    dest4.price = 1200
    dest4.image='destination_4.jpg'

    dest5 = destination()
    dest5.name="Madkeri"
    dest5.des = "The land of coffee"
    dest5.price = 1200
    dest5.image= 'destination_5.jpg'
    dest5.offer = True

    dest6 = destination()
    dest6.name="shivmogaa"
    dest6.des = "The land of coffee"
    dest6.price = 1200
    dest6.image='destination_6.jpg'
    
    dests = [dest1,dest2,dest3,dest4,dest5,dest6]

    return render(request,'index.html',{'dests':dests})