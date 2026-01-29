from space_network_lib import TemporalInterferenceError, DataCorruptedError, LinkTerminatedError, CommsError, OutOfRangeError
import time
class BrokenConnectionError(CommsError):
    pass
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
    except LinkTerminatedError:
        print("link lost")
        raise BrokenConnectionError()
    except OutOfRangeError:
        print("Target out of range")
        raise BrokenConnectionError()