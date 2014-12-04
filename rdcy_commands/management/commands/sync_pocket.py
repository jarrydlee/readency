from django.core.management.base import BaseCommand, CommandError
from base.models import Profile, ServiceConnection
from rdcy_api.pocket_api import PocketApi
from rdcy_api.kimono_api import KimonoApi
#from rdcy_managers.pocket_manager import PocketArticleManager

class Command(BaseCommand):

    def handle(self, *args, **options):
        pocket_instance = None
        kimono_instance = None
        
        profiles = Profile.objects.all()

        for profile in profiles:

            # Create the pocket instance
            pocket_instance = PocketApi(profile.access_token)
            connections = ServiceConnection.objects.filter(is_active=True)

            for connection in connections:

                # Create api instance for connection and get urls
                kimono_instance = KimonoApi(connection.service.api_endpoint, connection.num_articles)
                kimono_results = kimono_instance.get_results()

                # Get list of dict's containing pocket item information
                status_list = pocket_instance.bulk_add(kimono_results)

                # Store pocket information 
                #TODO
