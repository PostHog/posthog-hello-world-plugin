from posthog.plugins import PluginBaseClass, PosthogEvent


class ExamplePlugin(PluginBaseClass):
    @staticmethod
    def instance_init():
        ExamplePlugin.hello = "world"

    def team_init(self):
        self.hello = "hello"

    def process_event(self, event: PosthogEvent):
        event.properties["instance"] = ExamplePlugin.hello
        event.properties["team"] = self.hello
        return event
