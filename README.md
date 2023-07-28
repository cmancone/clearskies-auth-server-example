Register and create new tenant
Register for tenant
Login
Switch tenant
Modify my profile
Join another tenant
View my organizations
JWKS
CRUD users in tenant

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt"
            ],
            "Resource": "arn:aws:kms:[REGION]:[ACCOUNT_ID]:key/[kms-arn]"
        }
    ]
}
```

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:PutSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:[REGION]:[ACCOUNT_ID]:secret:/path/to/private",
                "arn:aws:secretsmanager:[REGION]:[ACCOUNT_ID]:secret:/path/to/public"
            ]
        }
    ]
}
```

```
poetry install
export AWS_REGION='us-east-1'
poetry run python key_manager.py --request_method=POST
poetry run python key_manager.py
```

```
uwsgi --http :9090 -H .venv --wsgi-file auth_service.py
```

```
curl 'http://localhost:9090/roles' -d '{"name": "Admin"}'
export ORGANIZATION_ID=$(curl 'http://localhost:9090/register_tenant' -d '{"name": "Conor", "email": "cmancone@example.com", "password": "thisisabadpassword", "repeat_password": "thisisabadpassword"}' | jq -r '.data.organization_id')
export JWT=$(curl "http://localhost:9090/login/$ORGANIZATION_ID" -d '{"email":"cmancone@example.com","password":"thisisabadpassword"}' | jq -r '.token')
curl 'http://localhost:9090/profile/my-organizations' -H "Authorization: Bearer $JWT"
curl "http://localhost:9090/login/switch/$ORGANIZATION_ID" -H "Authorization: Bearer $JWT"
curl "http://localhost:9090/profile" -d '{"name":"bob"}' -H "Authorization: Bearer $JWT"
```
