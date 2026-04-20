"""Stub de licențiere — licența este întotdeauna considerată validă."""
from __future__ import annotations

from homeassistant.core import HomeAssistant

LICENSE_API_URL = ""
STORAGE_KEY = "eonromania_license"
STORAGE_VERSION = 1
_FP_SALT = ""
INTEGRATION = "eonmyline"
SERVER_PUBLIC_KEYS_PEM: list[str] = []
SERVER_PUBLIC_KEY_PEM = ""


class LicenseManager:
    """Manager de licențe stub — întotdeauna valid, fără apeluri la server."""

    def __init__(self, hass: HomeAssistant) -> None:
        self._hass = hass
        self._data: dict = {}
        self._status_token: dict | None = None

    async def async_load(self) -> None:
        pass

    async def async_check_status(self) -> None:
        pass

    async def async_heartbeat(self) -> None:
        pass

    async def async_activate(self, license_key: str) -> dict:
        return {"success": True}

    async def async_deactivate(self) -> dict:
        return {"success": True}

    async def async_notify_event(self, action: str) -> None:
        pass

    async def _async_reload_entries(self) -> None:
        pass

    @property
    def is_valid(self) -> bool:
        return True

    @property
    def is_licensed(self) -> bool:
        return True

    @property
    def is_trial_valid(self) -> bool:
        return False

    @property
    def status(self) -> str:
        return "licensed"

    @property
    def license_type(self) -> str | None:
        return "perpetual"

    @property
    def license_key_masked(self) -> str | None:
        return None

    @property
    def trial_days_remaining(self) -> int:
        return 0

    @property
    def activated_at(self) -> float | None:
        return None

    @property
    def license_expires_at(self) -> float | None:
        return None

    @property
    def needs_heartbeat(self) -> bool:
        return False

    @property
    def check_interval_seconds(self) -> int:
        return 86400

    @property
    def fingerprint(self) -> str:
        return "stub"

    @property
    def hardware_fingerprint(self) -> str:
        return "stub"
