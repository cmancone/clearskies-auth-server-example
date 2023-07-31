import clearskies_aws
import clearskies_auth_server
import app
import logging

#logging.basicConfig(level=logging.DEBUG)

auth_service = clearskies_aws.contexts.wsgi(
    app.app,
    bindings={
        "secrets": clearskies_aws.secrets.SecretsManager,
    },
    binding_modules=[app.models],
)
def application(env, start_response):
    return auth_service(env, start_response)
