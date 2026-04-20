"""Button platform for my_smart_blinds_ble_proxy."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.my_smart_blinds_ble_proxy.const import PARALLEL_UPDATES as PARALLEL_UPDATES
from homeassistant.components.button import ButtonEntityDescription

from .reset_filter import ENTITY_DESCRIPTIONS as RESET_DESCRIPTIONS, MySmartBlindsBLEProxyButton

if TYPE_CHECKING:
    from custom_components.my_smart_blinds_ble_proxy.data import MySmartBlindsBLEProxyConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

# Combine all entity descriptions from different modules
ENTITY_DESCRIPTIONS: tuple[ButtonEntityDescription, ...] = (*RESET_DESCRIPTIONS,)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: MySmartBlindsBLEProxyConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the button platform."""
    async_add_entities(
        MySmartBlindsBLEProxyButton(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )
