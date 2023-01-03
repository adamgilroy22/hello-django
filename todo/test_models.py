from django.test import TestCase
from .models import Item


# Create your tests here.
class TestModels(TestCase):

    '''
    1. create a new item instance
    2. check that item.done is False

    '''
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    '''
    1. create a new item instance
    2. Check it equals to the string returned by the __str__
       method i.e. self.name

    '''
    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')

    '''
    1. Create an item Instance
    2. Edit the item using Post to “Updated Name”
    3. Check it redirects to home
    4. Save the edited item as updated_item
    5. Check this edited item equals "Updated Name”

    '''
    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
