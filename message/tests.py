from django.test import SimpleTestCase 
#nokte mohem:baraye zamani ke az database estefade nmikonim hamin SimpleTestCase okye
from django.urls import reverse

class MessagePageTests(SimpleTestCase):

    def test_url_exist_at_correct_location(self):
        response = self.client.get("/message/")
        #migim url message ro ersal kon az tarigh get request va pasokhesh ro baraye man save kon
        self.assertEqual(response.status_code , 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('message')) #inja chon mikhahim name ro test konim bayad az method reverse estefade konim
        self.assertEqual(response.status_code , 200)

    def test_template_name(self):
        response = self.client.get(reverse('message')) #inja ham ba reverse mishe ham ba url ama reverse rahattare
        self.assertTemplateUsed(response , 'home.html') #mire az response template ke bargashte ro name ro estekhraj mikone ba home.html moghayese mikone

    def test_template_content(self):
        response = self.client.get('/message/')
        self.assertContains(response , '<h1>This is a message☻</h1>')
        