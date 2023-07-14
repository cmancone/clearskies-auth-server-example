import clearskies_aws
import clearskies_auth_server

key_manager = clearskies_aws.contexts.cli(
    clearskies_auth_server.applications.key_manager(
        path_to_public_keys="/auth/test/public_keys",
        path_to_private_keys="/auth/test/private_keys",
    ),
    bindings = {
        "secrets": clearskies_aws.secrets.SecretsManager,
    }
)
key_manager()
