"""
Config flow handler package for my_smart_blinds_ble_proxy.

This package implements the configuration flows for the integration, organized
for maintainability and scalability.

Package structure:
------------------
- config_flow.py: Main configuration flow (user setup, reauth, reconfigure)
- options_flow.py: Options flow for post-setup configuration changes
- subentry_flow.py: Template for implementing subentry flows (multi-device support)
- schemas/: Voluptuous schemas for all forms (user, options, reauth, etc.)
- validators/: Validation logic for user inputs and credentials
- handler.py: Backwards compatibility wrapper (imports from above modules)

Usage:
------
The main config flow handler is imported in config_flow.py at the integration root:

    from .config_flow_handler import MySmartBlindsBLEProxyConfigFlowHandler

For more information:
https://developers.home-assistant.io/docs/config_entries_config_flow_handler
"""

from __future__ import annotations

from .config_flow import MySmartBlindsBLEProxyConfigFlowHandler
from .options_flow import MySmartBlindsBLEProxyOptionsFlow

__all__ = [
    "MySmartBlindsBLEProxyConfigFlowHandler",
    "MySmartBlindsBLEProxyOptionsFlow",
]
