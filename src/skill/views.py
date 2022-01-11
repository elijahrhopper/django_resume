from django.shortcuts import redirect, render

from skill.models import Skill

# Create your views here.
def home_view(request):
    skills = Skill.objects.all()

    if request.method == 'POST':
        new_skill = Skill(
            title = request.POST['title'],
            level = request.POST['level'],
            type = request.POST['type']
        )
        new_skill.save()
        return redirect('/')

    return render(request, 'home.html', {'skills': skills})

def delete_view(request, pk):
    skill = Skill.objects.get(id = pk)
    skill.delete()
    return redirect('/')