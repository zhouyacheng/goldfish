from typing import Any,Dict

from django.conf import settings
from rest_framework.settings import APISettings

COMMON_DEFAULTS: Dict[str,Any] = {
    "PAGE_SIZE_QUERY_PARAM": "size",
    "MAX_PAGE_SIZE": 100,
    "AUTHENTICATION_KEYWORD": "Bearer",
    "AUTHENTICATION_TOKEN_ALIVE_TIME": int(24 * 60 * 60 * 7),  # 秒
    "AUTHENTICATION_STORE_CACHE_NAME": "default",
    "AUTHENTICATION_STORE_CACHE_PREFIX": "auth",
}

IMPORT_STRINGS = []

common_settings = APISettings(
    user_settings=getattr(settings,"COMMON_SETTINGS",{}),
    defaults=COMMON_DEFAULTS,
    import_strings=IMPORT_STRINGS,
)