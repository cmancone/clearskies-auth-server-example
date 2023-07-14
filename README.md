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
