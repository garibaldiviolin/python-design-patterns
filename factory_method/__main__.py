from .classes import FedExFactory, DHLFactory


fedex = FedExFactory.create()
fedex.deliver()

dhl = DHLFactory.create()
dhl.deliver()
