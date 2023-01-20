from fastapi import FastAPI
from src.app.homepage.homepage import homepage_router
from src.app.prime.prime import prime_router

app = FastAPI(
    title="ue-nsi-zp-project",
    description="""
    Authorize data:
    - Enabled user:
    Login: test
    Password: zaq1@WSX
    - Disabled user:
    Login: test2
    Password: cde3$RFV
    """,
    version="0.0.1",
    license_info={
        "name": "MIT",
        "url": "https://github.com/rbrauner/uekat-studies-zp-project/blob/main/LICENSE",
    },
)
app.include_router(homepage_router)
app.include_router(prime_router)
