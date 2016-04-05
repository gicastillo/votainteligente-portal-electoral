# coding=utf-8
from django.core.urlresolvers import reverse
from elections.tests import VotaInteligenteTestCase as TestCase
from django.contrib.auth.models import User
from popular_proposal.models import ProposalTemporaryData, PopularProposal
from popular_proposal.forms import ProposalTemporaryDataUpdateForm
from popolo.models import Area


PASSWORD = 'perrito'


class BackendCitizenViewsTests(TestCase):
    def setUp(self):
        super(BackendCitizenViewsTests, self).setUp()
        self.fiera = User.objects.get(username='fiera')
        self.fiera.set_password(PASSWORD)
        self.fiera.save()
        self.arica = Area.objects.get(id='arica-15101')
        self.data = {
            'problem': u'A mi me gusta la contaminación de Santiago y los autos y sus estresantes ruedas',
            'solution': u'Viajar a ver al Feli una vez al mes',
            'when': u'1_year',
            'allies': u'El Feli y el resto de los cabros de la FCI'

        }

    def test_my_profile_view(self):
        url = reverse('backend_citizen:index')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('auth_login')+"?next="+url)
        self.client.login(username=self.fiera.username, password=PASSWORD)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'backend_citizen/index.html')

    def test_temporary_promise_detail_view(self):
        temporary_data = ProposalTemporaryData.objects.create(proposer=self.fiera,
                                                              area=self.arica,
                                                              data=self.data)
        url = reverse('backend_citizen:temporary_data_update', kwargs={'pk': temporary_data.id})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('auth_login')+'?next=' + url)
        self.client.login(username=self.fiera.username, password=PASSWORD)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'backend_citizen/temporary_data_update.html')
        self.assertIsInstance(response.context['form'], ProposalTemporaryDataUpdateForm)
        form = response.context['form']
        self.assertEquals(form.temporary_data, temporary_data)