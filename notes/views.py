from django.shortcuts import render
from django.views import View
from .forms import FormNote
from .models import Note
from django.http import HttpResponse, JsonResponse


def main_page(request):
    form = FormNote(request.POST or None)
    notes = Note.objects.all().order_by('-unique_words')

    return render(request, 'index.html', locals())


def check_unique_words(line):
    line = line.lower().split()
    answer = {item: 0 for item in line}
    for item in line:
        if item in answer:
            answer[item] += 1
    count_word = 0
    for item in answer.keys():
        if answer[item] == 1:
            count_word += 1
    return count_word


def add_note(request):
    if request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        unique_words = check_unique_words(text)

        Note.objects.create(author=author, text=text, unique_words=unique_words)

    notes = Note.objects.all().order_by('-unique_words')
    list_note = dict()
    list_note['notes'] = list()
    for item in notes:
        dict_note = dict()
        dict_note['author'] = item.author
        dict_note['text'] = item.text
        dict_note['unique_words'] = item.unique_words
        dict_note['created'] = item.created
        list_note['notes'].append(dict_note)

    return JsonResponse(list_note)
