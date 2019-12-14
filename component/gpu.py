from component.data import Component


class GPU(Component):
    def __init__(self, name, creation_date, manufacturer):
        super().__init__(name, creation_date, manufacturer)

    def get_specs(self):
        print(self.get_component_data())