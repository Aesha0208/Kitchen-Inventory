from django.urls import path
from newapp import views as v

urlpatterns = [
    path('Home/',v.home,name="home"),
    path('ContactUs/',v.contact,name="contactUs"),
    path('AboutUs/',v.about,name="aboutUs"),
    path('kitchen/details/',v.kitchenInv,name="kitchenInv"),
    path('addInv/',v.AddInv,name="addInv"),
    path('createInv/',v.CreateInv,name="CreateInv"),
    path('updateInv/',v.UpdateInvList,name="updateInvList"),
    path('updateInv/<str:id>',v.UpdateInv,name="updateInv"),
    path('delInv/<str:id>',v.DelInv,name="delInv"),
   
]