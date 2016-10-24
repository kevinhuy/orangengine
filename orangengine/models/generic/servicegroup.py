
class ServiceGroup(object):

    def __init__(self, name, elements=list()):
        """init a service group"""

        self.name = name
        self.elements = elements

    def add(self, service):
        """add a service"""

        self.elements.append(service)