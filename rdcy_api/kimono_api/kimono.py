from django.conf import settings
import requests
import json

class KimonoApi(object):
    url = settings.KIMONOLABS_URL
    api_key = settings.KIMONOLABS_KEY

    def __init__(self, api_code, num_articles):
        self.api_code = api_code
        self.num_articles = num_articles
        self.api_url = self._create_api_url()

    def _create_api_url(self):
        return self.url + self.api_code + '?apikey=' + self.api_key

    def _scrape_api(self):
        api_results = requests.get(self.api_url)
        api_results = json.loads(api_results.text)
        return api_results

    def _filter_results(self):
        link_list = []
        filter_results = self._scrape_api()

        for i, item in enumerate(filter_results['results']['links']):
            link_list.append(item['title']['href'])
            if i >= self.num_articles:
                break
        return link_list

    def get_results(self):
        return self._filter_results()


