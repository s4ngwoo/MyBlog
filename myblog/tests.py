from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post, Comment, Category, Tag, Series



# Create your tests here.

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # 0. 유저 언어 알아내기
        response = self.client.get('google.com')
        request = response.wsgi_request
        user_langs = request.META.get('HTTP_ACCEPT_LANGUAGE', ['en-US', ])
        print(f"User lang is {user_langs}")

        # 1. 리스트 가져오기
        # response = self.client.get('/')
        # self.assertEqual(response.status_code, 200)
        # # 1-1. 포스트 목록 가져오기

        # # 1-2. 타이틀 확인
        # soup = BeautifulSoup(response.content, 'html.parser')
        # self.assertEqual(soup.title.text, "Home")
        # # 1-3. 헤더 확인
        # #     1-3-1. 로고 확인
        # self.assertContains(response, '<img class="logo" src="')
        # #     1-3-2. 네비 이름 확인
        # navi = soup.header.nav.ul.text
        # self.assertIn('자기소개', navi)
        # self.assertIn('연락처', navi)
        # self.assertIn('보관소', navi)
        # #     1-3-3. 검색창 확인
        # # 1-4. 푸터 확인
        # self.assertIn('푸터', soup.footer.text)

        # # 2. 게시물이 없으면 없다고 띄우기
        # # 2-1. 게시물 갯수 확인
        # self.assertEqual(Posts.objects.count(), 0)
        # content = soup.find('section')
        # self.assertIn('아직 게시물이 없습니다', soup.main.text)
        # # 2-2. 게시물 갯수가 0 일때 '게시물이 없습니다 띄우기'


