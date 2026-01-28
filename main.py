from satellite import Satellite
from space_network_lib import SpaceEntity, SpaceNetwork, Packet

network = SpaceNetwork(2)
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
packet1 = Packet("hello my friend", sat1, sat2)
network.send(packet1)

