from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder
from src.backend.PluginManager.ActionInputSupport import ActionInputSupport
from src.backend.DeckManagement.InputIdentifier import Input

from .shared.logger import log as _log
from .features.tesmart.ip_switch_input import TESmartSwitchInput
from .features.tesmart.serial_switch_input import TESmartSerialSwitchInput
from .features.hdfury.switch_input import HDFurySwitchInput
from .features.tesmart.ip_manager import TESmartManager
from .features.tesmart.serial_manager import TESmartSerialManager
from .features.hdfury.manager import HDFuryManager

_ACTION_SUPPORT = {
    Input.Key: ActionInputSupport.SUPPORTED,
    Input.Dial: ActionInputSupport.UNSUPPORTED,
    Input.Touchscreen: ActionInputSupport.UNSUPPORTED,
}


class SwitchController(PluginBase):
    def __init__(self):
        super().__init__()

        try:
            import serial
            _log(f"pyserial {serial.VERSION} available")
        except ImportError:
            _log("pyserial not installed; serial actions will not work")

        self.tesmart = TESmartManager()
        self.tesmart_serial = TESmartSerialManager()
        self.hdfury = HDFuryManager()

        self.add_action_holder(ActionHolder(
            plugin_base=self,
            action_base=TESmartSwitchInput,
            action_id="dev_ninbura_SwitchController::TESmartSwitchInput",
            action_name="TESmart: Switch Input (IP)",
            action_support=_ACTION_SUPPORT,
        ))
        self.add_action_holder(ActionHolder(
            plugin_base=self,
            action_base=TESmartSerialSwitchInput,
            action_id="dev_ninbura_SwitchController::TESmartSerialSwitchInput",
            action_name="TESmart: Switch Input (Serial)",
            action_support=_ACTION_SUPPORT,
        ))
        self.add_action_holder(ActionHolder(
            plugin_base=self,
            action_base=HDFurySwitchInput,
            action_id="dev_ninbura_SwitchController::HDFurySwitchInput",
            action_name="HDFury: Switch Input (IP)",
            action_support=_ACTION_SUPPORT,
        ))

        self.register(
            plugin_name="Switch Controller",
            github_repo="https://github.com/ninbura/switch-controller",
            plugin_version="1.0.0",
            app_version="1.1.1-alpha"
        )
