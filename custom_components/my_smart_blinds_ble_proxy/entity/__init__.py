"""
Entity package for my_smart_blinds_ble_proxy.

Architecture:
    All platform entities inherit from (PlatformEntity, MySmartBlindsBLEProxyEntity).
    MRO order matters — platform-specific class first, then the integration base.
    Entities read data from coordinator.data and NEVER call the API client directly.
    Unique IDs follow the pattern: {entry_id}_{description.key}

See entity/base.py for the MySmartBlindsBLEProxyEntity base class.
"""

from .base import MySmartBlindsBLEProxyEntity

__all__ = ["MySmartBlindsBLEProxyEntity"]
