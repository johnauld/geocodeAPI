from geocoders.geocoder import Geocoder

class HereGeocoder(Geocoder):
    """Geocoder for here.com API"""
    def getProviderName(self):
        """Return a string with the name of this provider"""
        return 'here.com'
    
    def getParams( self, query ):
        """Return a dict with the parameters for the URL query string"""
        return {
            'app_id':       self.config['appId'],
            'app_code':     self.config['appCode'],
            'searchtext':   query,
        }

    def decodeResponse( self, response ):
        """Decode the response from the provider and return lat,lon"""
        location = response['Response']['View'][0]['Result'][0] \
                        ['Location']['NavigationPosition'][0]
        return location['Latitude'], location['Longitude']
