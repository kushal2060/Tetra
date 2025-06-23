from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def homepage(request):
    return render(request, 'homepage.html')

def games(request):
    return render(request, 'games.html')

def flappy_game(request):
    return render(request, 'flappy_game.html')


