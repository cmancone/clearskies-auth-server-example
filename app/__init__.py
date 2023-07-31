import clearskies
from . import models
from .login import login
from .profile import profile
from .registration import registration
from .roles import roles
from .users import users


app = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "authentication": clearskies.authentication.public(),
        "routes": [
            login,
            registration,
            roles, # don't do this for production
            profile,
            users,
        ]
    }
)

__all__ = [
    "app",
    "login",
    "models",
]
