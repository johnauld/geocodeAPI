from abc import ABC, abstractmethod
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from json import loads

class Geocoder(ABC):
    """Base class for all geocoders"""
    def __init__( self, config ):
        """Constructor"""
        self.config = config[self.__class__.__name__]

    def getLatLon( self, query ):
        """Invoke the underlying geocoding service and return result"""
        url = self.config['baseURL'] + '?' + urlencode(self.getParams(query))

        print(url)
        request = Request(url)

        respStr = urlopen( request, None, float(self.config['timeout']) )   \
            .read().decode()

        return self.decodeResponse( loads(respStr) )

    @abstractmethod
    def getProviderName(self):
        """Return a string with the name of this provider"""
        pass

    @abstractmethod
    def getParams( self, query ):
        """Return a dict with the parameters for the URL query string"""
        pass
    
    @abstractmethod
    def decodeResponse( self, response ):
        """Decode the response from the provider and return lat,lon"""
        pass
