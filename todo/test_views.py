from django.test import TestCase
from .models import Item


# Create your tests here.
class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)


class TestViews(TestCase):

    '''
    1. Save the homepage instance ("/") as response
    2. check that the response code is 200
    3. check that the template used, "todo/todo_list.html" is the same
       as "response"

    '''
    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    '''
    Similar to test_get_todo_list.

    '''
    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    '''
    1. create an Item Object
    2. save the response for that item
    3. assert this item response code is 200
    4. assert the template used is "edit_item.html"

    '''
    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    '''
    1. Create a new item
    2. check it redirects to the home page

    '''
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    '''
    1. Create a new item
    2. delete this item
    3. assert that it redirects to the home page
    4. Try to return the item from the database using filter and the item_id
    5. Check the length of existing_items = 0

    '''
    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    '''
    1. Create a new item object instance with done=True
    2. toggle this item so done=False
    3. assert that it redirects to the home page
    4. Get the item again and save as updated_item
    5. Check the done status is False

    '''
    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
