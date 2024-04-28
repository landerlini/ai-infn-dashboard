from os import environ as env
import json

HOST = env.get("AIINFN_HOST", "0.0.0.0")
PORT = int(env.get("AIINFN_PORT", "8080"))
DEBUG = env.get("AIINFN_DEBUG", "yes").lower() in ["y", "yes", "true"]
PROXY_PASS = env.get("AIINFN_PROXY_PASS", None)
FLASK_SECRET = env["FLASK_SECRET"]
SELF_SIGN_SSL_CERTIFICATE = env.get("SELF_SIGN_SSL_CERTIFICATE", "False").lower() in ["y", "yes", "true"]

IAM_SERVER = env.get('IAM_SERVER', "https://iam.cloud.infn.it")
IAM_SCOPES = json.loads(env.get("IAM_SCOPES", '["openid", "profile", "wlcg.groups"]'))
IAM_CLIENT_ID = env['IAM_CLIENT_ID']
IAM_CLIENT_SECRET = env['IAM_CLIENT_SECRET']
IAM_REDIRECT_URI = env.get("IAM_REDIRECT_URI", f"https://localhost:{PORT}/callback")
OIDC_CLOCK_SKEW = int(env.get("OIDC_CLOCK_SKEW", f"1"))

