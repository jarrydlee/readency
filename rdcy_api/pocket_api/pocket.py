from django.conf import settings
from pocket import Pocket

class PocketApi(object):

    pocket_instance = None

    def __init__(self, pocket_access_token):
        self.pocket_instance = Pocket(
            consumer_key=settings.POCKET_CONSUMER_KEY, 
            access_token=pocket_access_token
            )

    def add(self, url):
        return self.pocket_instance.add(url)

    def bulk_add(self, url_list):
        status_list = []
        
        for url in url_list:
            status_list.append(self.add(url=url))

        return status_list

    def delete(self, item_id):
        self.pocket_instance.delete(item_id)


