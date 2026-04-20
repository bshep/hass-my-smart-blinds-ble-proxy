"""
Config flow for my_smart_blinds_ble_proxy.

This module provides backwards compatibility for hassfest.
The actual implementation is in the config_flow_handler package.
"""

from __future__ import annotations

from .config_flow_handler import MySmartBlindsBLEProxyConfigFlowHandler

__all__ = ["MySmartBlindsBLEProxyConfigFlowHandler"]
