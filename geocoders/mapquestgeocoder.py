from geocoders.geocoder import Geocoder

class MapQuestGeocoder(Geocoder):
    """Geocoder for MapQuest API"""
    def getProviderName(self):
        """Return a string with the name of this provider"""
        return 'MapQuest'

    def getParams( self, query ):
        """Return a dict with the parameters for the URL query string"""
        return {
            'key':      self.config['apiKey'],
            'location': query
        }

    def decodeResponse( self, response ):
        """Decode the response from the provider and return lat,lon"""
        location = response['results'][0]['locations'][0]['latLng']
        return location['lat'], location['lng']
