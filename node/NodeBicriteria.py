import Node as node

class NodeBicriteria(node.Node) :
    def __init__(self, index, longitude, latitude) :
        node.Node.__init__(self, index, longitude, latitude)
        self.distance = 0
        self.danger = 0

class NodeLabelSetting(NodeBicriteria) :
    def __init__(self, index, longitude, latitude) :
        NodeBicriteria.__init__(self, index, longitude, latitude)
        self.labelList = []

class NodeBidirection(NodeBicriteria) :
    def __init__(self, index, longitude, latitude) :
        NodeBicriteria.__init__(self, index, longitude, latitude)
        fwLabelList = [] # forward labelList
        bwLabelList = [] # backward labelList
        self.directedLabelList = {
            True : fwLabelList,
            False : bwLabelList
        }
        
