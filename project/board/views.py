from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Board, Card
from django.utils.text import slugify


def list_of_board(request):
    """Return list of created and stored boards by user."""
    board = Board.objects.all()
    template = 'board/board.html'
    context = {'board': board}
    return render(request, template, context)


def board_detail(request, slug, board_id):
    """Return detail of specific board, shows assigned cards."""
    board = Board.objects.get(slug=slug, pk=board_id)
    context = {'board': board}
    template = 'board/board_detail.html'
    return render(request, template, context)


def create_board(request):
    """Receive data send by form.js script.
    Client side form validation is too weak, someone can use tool like POSTMAN,
    and send request with POST method with incorrect data to DB."""
    if request.method == 'POST':
        slug = request.POST['title']
        good_slug = slugify(slug)
        title = request.POST['title']
        good_title = " ".join(title.split())
        description = request.POST['description'].strip()
        category = request.POST['category'].strip()
        if title.isspace() or description.isspace() or category.isspace():
            return HttpResponse(status=405)
        else:
            if (len(good_title) >= 5 and len(description) >= 5 and len(category) >= 5 and len(good_slug) > 0) and \
                    (len(good_title) <= 15 and len(description) <= 25 and len(category) <= 25):
                obj, created = Board.objects.get_or_create(title=good_title,
                                                           defaults=
                                                           {'description': description,
                                                            'category': category,
                                                            'slug': good_slug})
                if created:
                    return HttpResponse(status=200)
                else:
                    return HttpResponse(status=406)
            else:
                return HttpResponse(status=409)
    else:
        return HttpResponse(status=400)


def create_card(request):
    """Receive data send by form_cards.js script.
    Client side form validation is too weak, someone can use tool like POSTMAN,
    and send request with POST method with incorrect data to DB."""
    if request.method == 'POST':
        title_board = request.POST['board_name']
        title_card = request.POST['title_card']
        good_title_card = " ".join(title_card.split())
        description_card = request.POST['description_card'].strip()
        unique_board = Board.objects.get(title=title_board)
        if title_card.isspace() or description_card.isspace():
            return HttpResponse(status=405)
        else:
            if (len(good_title_card) >= 5 and len(description_card) >= 5) and \
                    (len(good_title_card) <= 15 and len(description_card) <= 15):
                obj, created = Card.objects.get_or_create(title_card=good_title_card, board=unique_board,
                                                          defaults=
                                                          {'description_card': description_card})

                if created:
                    return HttpResponse(status=200)
                else:
                    return HttpResponse(status=406)
            else:
                return HttpResponse(status=409)
    else:
        return HttpResponse(status=400)


def delete_board(request, slug, board_id):
    """Delete board from boards list."""
    if request.method == 'DELETE':
        board = get_object_or_404(Board, slug=slug, pk=board_id)
        board.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)


def delete_card(request, slug, card_id, board_id):
    """Delete card from specific board.
    Come back to specific board after deleting."""
    if request.method == "DELETE":
        card = Card.objects.get(pk=card_id)
        card.delete()
        return HttpResponseRedirect(reverse('board:board_detail', args=(slug, board_id)))
    else:
        return HttpResponse(status=409)


def success_button(request, slug, board_id, card_id):
    """Change card status to success status."""
    if request.method == 'POST':
        Card.objects.filter(pk=card_id).update(colors='card-success')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)


def warning_button(request, slug, board_id, card_id):
    """Change card status to warning status."""
    if request.method == 'POST':
        Card.objects.filter(pk=card_id).update(colors='card-warning')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)


def danger_button(request, slug, board_id, card_id):
    """Change card status to danger status."""
    if request.method == 'POST':
        Card.objects.filter(pk=card_id).update(colors='card-danger')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)
