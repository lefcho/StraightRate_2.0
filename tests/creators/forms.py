from django.test import TestCase
from StraightRate_2.creators.forms import DirectorBaseForm
from StraightRate_2.media.models import Director


class DirectorBaseFormTest(TestCase):

    def test_save_method_transforms_data_and_saves_director(self):
        data = {
            'first_name': ' tEst  ',
            'last_name': ' TESt ',
        }

        form = DirectorBaseForm(data)

        self.assertTrue(form.is_valid())

        director = form.save(commit=True)

        saved_director = Director.objects.get(pk=director.pk)
        self.assertEqual(saved_director.first_name, 'Test')
        self.assertEqual(saved_director.last_name, 'Test')
