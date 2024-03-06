from os import environ as env
import json

HOST = env.get("AIINFN_HOST", "0.0.0.0")
PORT = int(env.get("AIINFN_PORT", "8080"))
DEBUG = env.get("AIINFN_DEBUG", "yes").lower() in ["y", "yes", "true"]
PROXY_PASS = env.get("AIINFN_PROXY_PASS", None)
FLASK_SECRET = env["FLASK_SECRET"]

IAM_SERVER = env.get('IAM_SERVER', "https://iam.cloud.infn.it")
IAM_SCOPES = json.loads(env.get("IAM_SCOPES", '["openid", "profile", "wlcg.groups"]'))
IAM_CLIENT_ID = env['IAM_CLIENT_ID']
IAM_CLIENT_SECRET = env['IAM_CLIENT_SECRET']
IAM_REDIRECT_URI = env.get("IAM_REDIRECT_URI", f"http://localhost:{PORT}/callback")

