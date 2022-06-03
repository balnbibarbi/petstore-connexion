#!/usr/bin/env python

from connexion import FlaskApp
from connexion.resolver import RelativeResolver
import petstore

PORT=8080
API_NAME='petstore'
API_SPEC_DIR=API_NAME
API_SPEC_FILE=API_NAME + '.yaml'

if __name__ == "__main__":
    app = FlaskApp(
        __name__,
        specification_dir=API_SPEC_DIR,
        resolver=RelativeResolver(API_NAME)
    )
    app.add_api(API_SPEC_FILE, resolver_error=501)
    app.run(port=PORT)
