import clearskies_auth_server

self_authenticate = clearskies_auth_server.authentication.jwks_direct(
    path_to_public_keys='/auth/test/public_keys',
    audience='clearskies.auth.example.com',
    issuer='clearskies.auth.example.com',
)
