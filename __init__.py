from posthog.plugins import PluginBaseClass, PosthogEvent


class ExamplePlugin(PluginBaseClass):
    def __init__(self, config):
        self.bar = config['foo']
        pass
    
    def process_event(self, event: PosthogEvent):
        event.properties["hello"] = "world"
        event.properties["bar"] = self.bar
        return event
