from dataclasses import dataclass
from contextlib import contextmanager
import logging
from typing import List

# Flask
import flask

# Flask PyOIDC
from flask_pyoidc.provider_configuration import ClientMetadata, ProviderConfiguration
from flask_pyoidc import OIDCAuthentication
from flask_pyoidc.user_session import UserSession

# Local configuration
from . import configuration as cfg

@dataclass
class User:
    family_name: str
    given_name: str
    name: str
    groups: List[str]

    @staticmethod
    @contextmanager
    def from_session():
        userinfo = UserSession(flask.session).userinfo
        try:
            logging.getLogger("User").debug(f"Authenticated user session begins [{userinfo['preferred_username']}]")
            yield User(
                family_name=userinfo['family_name'],
                given_name=userinfo['given_name'],
                name=userinfo['preferred_username'],
                groups=[g[1:] if g[0] in '/' else g for g in userinfo["wlcg.groups"]]
            )
        finally:
            logging.getLogger("User").debug(f"End of authenticated session [{userinfo['preferred_username']}]")


def configure_authentication(flask_app):
    client_metadata = ClientMetadata(
        client_id=cfg.IAM_CLIENT_ID,
        client_secret=cfg.IAM_CLIENT_SECRET,
    )

    provider_config = ProviderConfiguration(
        issuer=cfg.IAM_SERVER,
        client_metadata=client_metadata,
        session_refresh_interval_seconds=1800,
        auth_request_params=dict(
            scope=cfg.IAM_SCOPES
        )
    )

    return OIDCAuthentication(dict(default=provider_config), flask_app)

