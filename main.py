from satellite import Satellite
from space_network_lib import SpaceNetwork, Packet, TemporalInterferenceError, DataCorruptedError
import time

network = SpaceNetwork(2)
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
packet1 = Packet("hello my friend", sat1, sat2)
while True:
    try:
        network.send(packet1)
    except (TemporalInterferenceError, DataCorruptedError) as e:
        if isinstance(e, TemporalInterferenceError):
            time.sleep(2)
            continue
        if isinstance(e, DataCorruptedError):
            continue
    break