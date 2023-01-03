from django.test import TestCase
from .forms import ItemForm


# Create your tests here.
class TestItemForm(TestCase):
    '''
    1. creates a form instance with an empty name field
    2. checks this field is not valid
    3. checks that there is a "name" key in the dictionary of form errors
    4. Check whether the error message on the name key is “This field is
       required.”

    '''
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    '''
    1. Create a form instance with a name field of "Test Todo Items"
    2. Checks that this instance is valid (even without selecting a "done"
       status)

    '''
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Items'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
