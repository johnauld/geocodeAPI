from geocoders.geocoder import Geocoder

class OpenCageDataGeocoder(Geocoder):
    """Geocoder for OpenCage Data API"""
    def getProviderName(self):
        """Return a string with the name of this provider"""
        return 'OpenCageData'
    
    def getParams( self, query ):
        """Return a dict with the parameters for the URL query string"""
        return {
            'geocoding-type':   'forward',
            'key':              self.config['apiKey'],
            'q':                query,
        }

    def decodeResponse( self, response ):
        """Decode the response from the provider and return lat,lon"""
        location = response['results'][0]['geometry']
        return location['lat'], location['lng']
