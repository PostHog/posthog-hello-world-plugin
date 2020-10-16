from posthog.plugins import PluginBaseClass, PosthogEvent


class ExamplePlugin(PluginBaseClass):
    def process_event(self, event: PosthogEvent):
    event.properties["hello"] = "world"
    event.properties["bar"] = self.config["bar"]
    return event
