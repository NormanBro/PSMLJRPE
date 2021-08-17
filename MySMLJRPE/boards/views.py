from django.shortcuts import render, get_list_or_404

from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board=get_list_or_404(Board,pk=pk)
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})