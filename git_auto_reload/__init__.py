try:
    import rest_api
except (ImportError, ModuleNotFoundError):
    rest_api = None  # ty: ignore[invalid-assignment]
from mcdreforged.api.all import PluginServerInterface
from git_auto_reload.command import register


def on_load(s: PluginServerInterface, _):
    global rest_api
    register(s)
    if not rest_api:
        rest_api = s.get_plugin_instance("rest_api")
    s.logger.info("GitAutoReload loaded.")


def on_unload(s: PluginServerInterface):
    s.logger.info("GitAutoReload unloaded.")


@rest_api.webhook(
    "git_auto_reload", summary="GitAutoReload debugger.", require_auth=True
)
async def on_debug_webhook(data: dict):
    """Debug port. Return the data posted."""
    return data
