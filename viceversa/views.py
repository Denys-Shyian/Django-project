import string

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_test = user_text[::-1]
    number_of_words = sum([i.strip(string.punctuation).isalpha() for i in user_text.split()])

    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_test,
                                            'numberofwords': number_of_words})
