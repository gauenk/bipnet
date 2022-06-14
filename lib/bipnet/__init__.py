from . import burst_deno
from . import burst_sr
from . import utils

def load_deno_network(mode="color"):
    weights = "/home/gauenk/Documents/packages/bipnet/weights/BIPNet.ckpt"
    network = burst_deno.BIPNet(mode)
    network = network.load_from_checkpoint(weights, mode='color')
    return network


