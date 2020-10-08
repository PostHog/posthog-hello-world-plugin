from posthog.plugins import PluginBaseClass, PosthogEvent


class ExamplePlugin(PluginBaseClass):
    def __init__(self, config):
        pass
    
    def process_event(self, event: PosthogEvent):
        event.properties["hello"] = "world"
        return event
