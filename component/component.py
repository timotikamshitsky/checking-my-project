class Component:
    name: str
    creation_date: int
    manufacturer: str

    def __init__(self, name, creation_date, manufacturer):
        self.name = name
        self.creation_date = creation_date
        self.manufacturer = manufacturer

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_creation_date(self, date):
        self.creation_date = date

    def get_creation_date(self):
        return self.creation_date

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def get_component_data(self):
        return self.get_name(), self.get_creation_date(), self.get_manufacturer()
