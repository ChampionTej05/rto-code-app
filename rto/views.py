from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import RTOCode
from django.template import loader
# Create your views here.


def home(request):
    template = loader.get_template('rto/input.html')
    context = {}
    return HttpResponse(template.render(context, request))


def findCity(request):
    try : 
        state_name = request.POST['state_name'].upper()
        city_code = request.POST['city_code'].lstrip('0')
        print("State Name:",state_name)
        print("City Code:",city_code)
        obj_list = RTOCode.objects.filter(state_name=state_name).filter(city_code=city_code)
        print(obj_list)
        response = "Result : "
        if len(obj_list) != 0 :
            obj_list= obj_list.values()[0]
            response += "Object Found with the State Name = "+state_name + " , and City Code : "+ city_code + " <br></br>  <h2>"+ str(obj_list["city_name"]) +"</h2>"
        else:
            response += "No Object Found with the State Name = "+state_name + " , and City Code : "+ city_code
        return HttpResponse(response)
    except (RTOCode.DoesNotExist,KeyError,Exception) as err:
        return render(request,'rto/input.html',{'error_message':'Error in Form  '+str(err)})

def addCityToDB(state_name, city_code,city_name):
    try:
        city_objects = RTOCode.objects.create(state_name=state_name, city_code=city_code,city_name=city_name)
        city_objects.save()
        return 200
    except Exception as err:
        print("Exception: "+err)
        return 400


# use this  url when you need to add data to Database from rto_Codes.csv
def addCity(request):
    try : 
        import pandas as pd 
        af = pd.read_csv('/home/RakshitKathawate/rto-code-app/rto_codes.csv')
        # af = af.head()

        for idx, row in af.iterrows():
            state_name= row.state_name.upper()
            city_code = row.city_code.lstrip('0')
            city_name = row.city_name
            
            print("State Name:",state_name)
            print("City Code:",city_code)
            print("CityName : ",city_name)
            if addCityToDB(state_name=state_name, city_code=city_code,city_name=city_name) == 200 :
                pass
            else : 
                print("Sorry !!, something went wrong ")
        return HttpResponse ('Successfully added Data !!!')
    except Exception as err:
        return HttpResponse('Error Obtained: '+str(err))

def findAll(request):

    obj_list= RTOCode.objects.all().order_by('state_name','city_code')
    # response = " , ".join([str(obj) for obj in obj_list])
    context= {'rto_codes':obj_list}
    return render(request,'rto/show.html',context)


def showError(request):

    # any errors there, show alert and redirect to home page
    return redirect("/")





