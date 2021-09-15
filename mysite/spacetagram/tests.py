import os
from mysite.settings import STATIC_ROOT
from django.test import TestCase
from django.contrib.staticfiles.storage import staticfiles_storage

class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # check if compiled Svelte build files load from static files directory
    def test_load_global_css(self):
        abs_path = os.path.join(STATIC_ROOT, 'global.css')
        self.assertTrue(staticfiles_storage.exists(abs_path))

    def test_load_bundle_css(self):
        abs_path = os.path.join(STATIC_ROOT, 'build/bundle.css')
        self.assertTrue(staticfiles_storage.exists(abs_path))

    def test_load_bundle_js(self):
        abs_path = os.path.join(STATIC_ROOT, 'build/bundle.js')
        self.assertTrue(staticfiles_storage.exists(abs_path))

    def test_load_bundle_js_map(self):
        abs_path = os.path.join(STATIC_ROOT, 'build/bundle.js.map')
        self.assertTrue(staticfiles_storage.exists(abs_path))

    def test_load_background_image(self):
        abs_path = os.path.join(STATIC_ROOT, 'img/space_image3.jpg')
        self.assertTrue(staticfiles_storage.exists(abs_path))






