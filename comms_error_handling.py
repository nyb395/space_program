from space_network_lib import TemporalInterferenceError, DataCorruptedError
import time
def attempt_transmission(packet: "Packet", network: "Network"):
    try:
        network.send(packet)
    except TemporalInterferenceError:
        print("Interference, waiting...")
        time.sleep(2)
        attempt_transmission(packet, network)
    except DataCorruptedError:
        print("Data corrupted, retrying...")
        attempt_transmission(packet, network)