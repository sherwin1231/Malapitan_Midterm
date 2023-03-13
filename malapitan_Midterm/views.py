from django.shortcuts import render
from django.http import HttpResponse

def Midterm_A(request):
    jobroles=['Reporting Executives', 'Business analyst', 'data analyst', 'Statistician', 'Data Scientist', 'Machine learning Engineer', 'Big Data Engineer'];
    
    for item in jobroles:
        letter_count=len(item)
       


    return render(request,"miterma.html",{'list':item, 'letter_count ':letter_count})

