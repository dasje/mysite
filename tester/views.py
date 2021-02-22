from django.shortcuts import render, get_object_or_404

def goforit(request):
    return render(request, 'tester.html', 
    	{'section': 'tester'},
    	)