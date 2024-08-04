class EntertainmentDevice:

    def connect_device_to_power_outlet(self, device):
        ...


class RcaCabel:
    def rda_connect_cable(self, obj):
        ...


class HdmiCabel:
    def hdmi_connect_cable(self, obj):
        ...


class EthernetCable:
    def ethernet_connect_cable(self, obj):
        ...


class Television(EntertainmentDevice, RcaCabel, HdmiCabel):
    def connect_to_dvd(self, dvd_player):
        super().rda_connect_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        super().hdmi_connect_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, HdmiCabel):
    def connect_to_tv(self, television):
        super().hdmi_connect_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, HdmiCabel, EthernetCable):
    def connect_to_tv(self, television):
        super().hdmi_connect_cable(television)

    def connect_to_router(self, router):
        super().ethernet_connect_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, EthernetCable):
    def connect_to_tv(self, television):
        super().ethernet_connect_cable(television)

    def connect_to_game_console(self, game_console):
        super().ethernet_connect_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
