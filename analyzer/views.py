from django.shortcuts import render
from .utils import analyze_code

def home(request):
    result = None
    code = ""
    language = "python"

    if request.method == "POST":
        code = request.POST.get("code", "")
        language = request.POST.get("language", "python")
        result = analyze_code(code, language)

    return render(request, "index.html", {
        "result": result,
        "code": code,
        "language": language
    })