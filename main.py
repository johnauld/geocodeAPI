import sys
from flask import Flask, jsonify, abort, make_response, request
from geocoders import Geocoder
from configparser import ConfigParser, BasicInterpolation

parser = ConfigParser(interpolation=BasicInterpolation())
parser.read('geocodeAPI.ini')
config = parser['main']

# Instantiate all service providers for later use
providers = [ instance(parser) for instance in Geocoder.__subclasses__() ]

app = Flask(__name__)

@app.route( config['geocodeURL'] )
def geocode():
    """Handler for geocoding service requests via geocodeURL"""
    addr = request.args.get( 'addr' )
    if addr is None or len(addr) == 0:
        abort(400)

    # Try each provider in turn. Log any exceptions, break if successful
    for provider in providers:
        try:
            providerName = provider.getProviderName()
            lat, lon = provider.getLatLon(addr)
            break
        except Exception as ex:
            print( 'Exception ('+providerName+'): '+str(ex), file=sys.stderr )
#             raise ex
        else:
            break   # Some provider succeeded
    else:
        print( 'Exhausted all providers', file=sys.stderr )
        abort(503)

    return jsonify( { 'status':     200             },
                    { 'msg':        'OK'            },
                    { 'provider':   providerName    },
                    { 'lat':        lat             },
                    { 'lon':        lon             },  )

@app.errorhandler(400)  # Bad request
@app.errorhandler(404)  # Not found
@app.errorhandler(503)  # Service unavailable   
def errorhandler(err):
    """HTTP error handler """
    return make_response(
        jsonify( {'status': err.code}, {'msg': err.description} ), err.code )

if __name__ == '__main__':
    app.run( port=int(config['httpPort']), debug=True )
