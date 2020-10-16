from posthog.plugins import PluginBaseClass, PosthogEvent

1 / 0
raise Exception("bla")
class ExamplePlugin(PluginBaseClass):
    def process_event(self, event: PosthogEvent):
        event.properties["hello"] = "world"
        event.properties["bar"] = self.config["bar"]
        return event
