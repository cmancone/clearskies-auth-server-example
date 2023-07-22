import clearskies
from . import models
from .login import login
from .registration import registration
from .roles import roles

app = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "authentication": clearskies.authentication.public(),
        "routes": [
            login,
            registration,
            roles, # don't do this for production
        ]
    }
)

__all__ = [
    "app",
    "login",
    "models",
]
