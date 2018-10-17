from django.test import TestCase
from .models import Board, Card
from django.shortcuts import reverse


class BoardTest(TestCase):
    def test_board(self):
        self.assertTrue(Board.objects.create(title='onlyboardtest', description="testing",
                                             category="testcase", slug="letstest"))


class CardTest(TestCase):
    def test_card(self):
        self.assertTrue(Card.objects.create(title_card='onlycardtestc', description_card="testing",
                                            board=Board.objects.create(title='onlyboardtest', description="testing",
                                                                       category="testcase", slug="testing")))


class ListViewsTestCase(TestCase):
    def test_list_of_board(self):
        response = self.client.get('/board/')
        self.assertEqual(response.status_code, 200)


class BoardDetailTestCase(TestCase):
    def test_board_detail_(self):
        test = Board.objects.create(title='onlyboardtest', description="testing", category="testcase", slug='letstest')
        response = self.client.get(reverse('board:board_detail', args=(test.slug,)))
        self.assertEqual(response.status_code, 200)


class BoardDeleteTestCase(TestCase):
    def test_delete_board(self):
        test = Board.objects.create(title='onlyboardtest', description="testing", category="testcase", slug='letstest')
        response = self.client.get(reverse('board:delete_board', args=(test.slug,)))
        self.assertEqual(response.status_code, 302)
