import os
import importlib


class PluginManager:
    """
    Handles loading and managing external plugins.
    """

    def __init__(self, plugins_directory="plugins"):

        self.plugins_directory = plugins_directory
        self.plugins = {}

        self.load_plugins()

    # --------------------------------------------------
    # LOAD PLUGINS
    # --------------------------------------------------

    def load_plugins(self):

        if not os.path.exists(self.plugins_directory):
            return

        for file in os.listdir(self.plugins_directory):

            if file.endswith(".py") and not file.startswith("_"):

                plugin_name = file[:-3]

                try:

                    module = importlib.import_module(f"{self.plugins_directory}.{plugin_name}")

                    if hasattr(module, "Plugin"):

                        plugin_class = getattr(module, "Plugin")
                        plugin_instance = plugin_class()

                        self.plugins[plugin_name] = plugin_instance

                        print(f"Plugin loaded: {plugin_name}")

                except Exception as e:

                    print(f"Failed to load plugin {plugin_name}: {e}")

    # --------------------------------------------------
    # EXECUTE PLUGIN
    # --------------------------------------------------

    def execute_plugin(self, plugin_name, command):

        plugin = self.plugins.get(plugin_name)

        if plugin:

            return plugin.run(command)

        return None

    # --------------------------------------------------
    # LIST PLUGINS
    # --------------------------------------------------

    def list_plugins(self):

        return list(self.plugins.keys())