from geocoders.geocoder import Geocoder

class GoogleGeocoder(Geocoder):
    """Geocoder for Google API"""
    def getProviderName(self):
        """Return a string with the name of this provider"""
        return 'Google'

    def getParams( self, query ):
        """Return a dict with the parameters for the URL query string"""
        return {
            'key':      self.config['apiKey'],
            'address':  query
        }

    def decodeResponse( self, response ):
        """Decode the response from the provider and return lat,lon"""
        location = response['results'][0]['geometry']['location']
        return location['lat'], location['lng']
