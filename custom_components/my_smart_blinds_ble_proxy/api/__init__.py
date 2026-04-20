"""
API package for my_smart_blinds_ble_proxy.

Architecture:
    Three-layer data flow: Entities → Coordinator → API Client.
    Only the coordinator should call the API client. Entities must never
    import or call the API client directly.

Exception hierarchy:
    MySmartBlindsBLEProxyApiClientError (base)
    ├── MySmartBlindsBLEProxyApiClientCommunicationError (network/timeout)
    └── MySmartBlindsBLEProxyApiClientAuthenticationError (401/403)

Coordinator exception mapping:
    ApiClientAuthenticationError → ConfigEntryAuthFailed (triggers reauth)
    ApiClientCommunicationError → UpdateFailed (auto-retry)
    ApiClientError             → UpdateFailed (auto-retry)
"""

from .client import (
    MySmartBlindsBLEProxyApiClient,
    MySmartBlindsBLEProxyApiClientAuthenticationError,
    MySmartBlindsBLEProxyApiClientCommunicationError,
    MySmartBlindsBLEProxyApiClientError,
)

__all__ = [
    "MySmartBlindsBLEProxyApiClient",
    "MySmartBlindsBLEProxyApiClientAuthenticationError",
    "MySmartBlindsBLEProxyApiClientCommunicationError",
    "MySmartBlindsBLEProxyApiClientError",
]
