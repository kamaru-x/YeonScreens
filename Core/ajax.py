from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Core.models import Series,Application,Project,Event,Enquiry,Features,Specification,Works,Client
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def edit_feature(request):
    if request.method == 'POST':
        feature_id = request.POST.get('feature_id')
        title = request.POST.get('title')

        feature = Features.objects.get(id=feature_id)
        feature.Title = title
        feature.save()

    return JsonResponse({'status':'success'})

@csrf_exempt
def delete_feature(request):
    if request.method == 'POST':
        feature_id = request.POST.get('feature_id')
        feature = Features.objects.get(id=feature_id)
        feature.delete()

    return JsonResponse({'status':'success'})

@csrf_exempt
def edit_spec(request):
    if request.method == 'POST':
        spec_id = request.POST.get('spec_id')
        spec = Specification.objects.get(id=spec_id)
        spec.Title = request.POST.get('title')
        spec.Value = request.POST.get('value')
        spec.save()
    return JsonResponse({'status':'success'})

@csrf_exempt
def delete_spec(request):
    if request.method == 'POST':
        spec_id = request.POST.get('spec_id')
        spec = Specification.objects.get(id=spec_id)
        spec.delete()
    return JsonResponse({'status':'success'})