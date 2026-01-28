from space_network_lib import SpaceEntity, SpaceNetwork, Packet


class Satellite(SpaceEntity):
    def __init__(self, name, distance_from_earth):
        super().__init__(name, distance_from_earth)

    def receive_signal(self, packet: Packet):
        print(f"[{self.name}] Received: {packet}")


network = SpaceNetwork(1)
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
packet1 = Packet("hello my friend", sat1, sat2)
network.send(packet1)

