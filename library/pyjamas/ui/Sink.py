from pyjamas.ui.Composite import Composite
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Hyperlink import Hyperlink

class SinkList(Composite):
    def __init__(self):
        Composite.__init__(self)

        self.vp_list=VerticalPanel()
        self.sinks=[]
        self.selectedSink=-1
        
        self.initWidget(self.vp_list)
        self.setStyleName("ks-List")

    def add(self, info):
        name = info.getName()
        link = Hyperlink(name, False, TargetHistoryToken=name)
        link.setStyleName("ks-SinkItem")
        self.vp_list.add(link)
        self.sinks.append(info)

    def find(self, sinkName):
        for info in self.sinks:
            if info.getName()==sinkName:
                return info
        return None

    def setSinkSelection(self, name):
        if self.selectedSink <> -1:
            self.vp_list.getWidget(self.selectedSink).removeStyleName("ks-SinkItem-selected")

        for i in range(len(self.sinks)):
            info = self.sinks[i]
            if (info.getName()==name):
                self.selectedSink = i
                widget=self.vp_list.getWidget(self.selectedSink)
                widget.addStyleName("ks-SinkItem-selected")
                return


class Sink(Composite):
    def __init__(self):
        Composite.__init__(self)
    
    def onHide(self):
        pass
        
    def onShow(self):
        pass

    def baseURL(self):
        return ""

class SinkInfo:
    def __init__(self, name, desc, object_type):
        self.name=name
        self.description=desc
        self.object_type=object_type
        self.instance=None

    def createInstance(self):
        obj = self.object_type()
        obj.name = self.name
        return obj

    def getDescription(self):
        return self.description

    def getInstance(self):
        if self.instance is None:
            self.instance = self.createInstance()
        return self.instance
    
    def getName(self):
        return self.name
    
