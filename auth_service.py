import clearskies_aws
import clearskies_auth_server
import app

auth_service = clearskies_aws.contexts.wsgi(
    app,
    bindings={
        "secrets": clearskies_aws.secrets.SecretsManager,
    },
    binding_modules=[app.models],
)
def application(env, start_response):
    return auth_service(env, start_response)
