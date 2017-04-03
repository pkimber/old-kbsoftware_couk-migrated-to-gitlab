# -*- encoding: utf-8 -*-
import httplib2

from apiclient import errors
from apiclient.discovery import build
from django.core.management.base import BaseCommand
from oauth2client.client import OAuth2WebServerFlow
# from googleapiclient import sample_tools



# Copy your credentials from the console
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

# Check https://developers.google.com/webmaster-tools/search-console-api-original/v3/ for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly'

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'



class Command(BaseCommand):

    help = "SEO #2214"

    # def execute_request(self, service, property_uri, request):
    #   """Executes a searchAnalytics.query request.
    #   Args:
    #     service: The webmasters service to use when executing the query.
    #     property_uri: The site or app URI to request data for.
    #     request: The request to be executed.
    #   Returns:
    #     An array of response rows.
    #   """
    #   return service.searchanalytics().query(
    #       siteUrl=property_uri, body=request).execute()

    def handle(self, *args, **options):
        """
        613815634402-7kdsk6othf06q7p2cnpvk2v1eo5gpjf9.apps.googleusercontent.com
        0rREUkNThBWmAyF6kiaRSV_S

        """
        self.stdout.write("{}".format(self.help))
        # service, flags = sample_tools.init(
        #     argv,
        #     'webmasters',
        #     'v3',
        #     __doc__,
        #     __file__,
        #     parents=[argparser],
        #     scope='https://www.googleapis.com/auth/webmasters.readonly'
        # )

        # request = {
        #     'startDate': flags.start_date,
        #     'endDate': flags.end_date,
        #     'dimensions': ['date']
        # }


        # Run through the OAuth flow and retrieve credentials
        flow = OAuth2WebServerFlow(
            CLIENT_ID,
            CLIENT_SECRET,
            OAUTH_SCOPE,
            REDIRECT_URI,
        )
        authorize_url = flow.step1_get_authorize_url()
        self.stdout.write(
            'Go to the following link in your browser:\n'.format(authorize_url)
        )
        code = input('Enter verification code: ').strip()
        credentials = flow.step2_exchange(code)

        # Create an httplib2.Http object and authorize it with our credentials
        http = httplib2.Http()
        http = credentials.authorize(http)

        webmasters_service = build('webmasters', 'v3', http=http)

        # Retrieve list of properties in account
        site_list = webmasters_service.sites().list().execute()

        # Filter for verified websites
        verified_sites_urls = [s['siteUrl'] for s in site_list['siteEntry']
                if s['permissionLevel'] != 'siteUnverifiedUser'
                and s['siteUrl'][:4] == 'http']

        # Printing the URLs of all websites you are verified for.
        for site_url in verified_sites_urls:
            self.stdout.write(site_url)
            # Retrieve list of sitemaps submitted
            sitemaps = webmasters_service.sitemaps().list(siteUrl=site_url).execute()
            if 'sitemap' in sitemaps:
                sitemap_urls = [s['path'] for s in sitemaps['sitemap']]
                for url in sitemap_urls:
                    self.stdout.write("  {}".format(url))

        self.stdout.write("Complete...")
