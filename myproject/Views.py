from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        "ContactName" : ["Aarav", "Vivaan", "Aditya", "Vihaan", "Reyansh", "Ayaan", "Krishna", "Ishaan","Zoya", "Anaya", "Diya", "Saanvi", "Mira", "Kiara", "Myra", "Sara", "Kavya", "Tara"]
    }
    return render(request, 'home.html')
    # return render(request, 'forloop&IfCondition.html', data)
    # return HttpResponse('This is home page')

def aboutUs(request):
    data = {
        "ContactName" : ["Aarav", "Vivaan", "Aditya", "Vihaan", "Reyansh", "Ayaan", "Krishna", "Ishaan","Zoya", "Anaya", "Diya", "Saanvi", "Mira", "Kiara", "Myra", "Sara", "Kavya", "Tara"]
    }
    
    return render(request, 'About.html', data)
    # return HttpResponse('This is aboutUs page')

def ContactUs(request):
    return render(request, 'Contact.html')
    # return HttpResponse('This is ContactUs page')
    # return HttpResponse(No)

def Services(request):
    return render(request, 'Services.html')


def UserFormGETMethod(requests):
    intSum = 0
    data = {}
    
    try:
        n1 = requests.POST.get("FirstNumber")
        n2 = requests.POST.get("SecondNumber")
        intSum = int(n1) + int(n2)
        data = {
        "Sum": intSum,
        "Num1": n1,
        "Num2": n2
        }
    
    except Exception as e:
         pass
    
    
    print('enter in render_________________________')
    return render(requests, 'UserFormGETMethod.html', data)


