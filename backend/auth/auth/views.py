from django.contrib.auth.forms import UserCreationForm
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "ok"})
        return JsonResponse({"error": "Form is not valid"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
