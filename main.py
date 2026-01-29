from satellite import Satellite
from space_network_lib import SpaceNetwork, Packet
from comms_error_handling import attempt_transmission

network = SpaceNetwork(3)
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
packet1 = Packet("hello my friend", sat1, sat2)
attempt_transmission(packet1, network)
