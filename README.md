#### INTRODUCTION

This is a demonstration project implementing a very simple geocoding service
supporting multiple backends for resilience.

#### API USAGE

The service is accessed via HTTP `GET` operations on a configurable URL. The query
string provides a postal address (`addr`) which is passed to some backend
service provider for geocoding. Multiple providers can be configured, and each
is tried in turn until either a result is obtained, or all configured providers
have been tried.

The data is returned to the caller in JSON format, containing the following
fields:

- `status`     A numeric HTTP status code (`200` for success)
- `msg`        A friendly message corresponding to the status (e.g., `OK`)
        (the remaining fields are only provided if the status is `200`)
- `provider`   The name of the provider from which this data was obtained
- `lat`        Floating point degrees of latitude (negative for south)
- `lon`        Floating point degrees of longitude (negative for west)

The status code is also returned as the HTTP status for the `GET` request.

#### SERVICE CONFIGURATION

The configuration is stored in `geocodeAPI.ini`. The `[main]` section defines the
path component of the URL on which the service will be provided. Additional
sections, one for each backend provider class, define the timeout to be used
when interacting with that provider, as well as parameters specific to each
class such as the request.

#### INTERNAL STRUCTURE

`Geocoder` is an abstract base class that defines the internal API used by all
geocoder backend provider classes, as well as providing provider-independent
functionality.

Subclasses of `Geocoder` implement the provider-specific functionality. Adding a
new provider involves creating a class that implements the abstract methods of
`Geocoder`, adding a section for the new class to the config file, and adding a
reference to the class to the `geocoders` package's `__init__.py` module.
