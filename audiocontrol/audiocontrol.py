from pickletools import bytes1
from struct import pack
import pulsectl
import sys
sys.path.append("..")
from log.log import *

"""
Commands:
listsources
    returns: index:'name','description','mute','channels','volumes'|index:'name','description','mute','channels','volumes'|...
listsinks
    returns: index:'name','description','mute','channels','volumes'|index:'name','description','mute','channels','volumes'|...
getdefaultsource
    returns: id
setdefaultsource    id
getdefaultsink
    returns: id
setdefaultsink      id
getvolume           sink/source, id
    returns: volume_tuple
setvolume           sink/source, id, volume
incvolume           sink/source, id, value
decvolume           sink/source, id, value
getmute             sink/source, id
    returns: 0/1
setmute             sink/source, id, 1/0
togglemute          sink/source, id
    returns: new_mutevalue
"""


class audiocontrol(object):

    def __init__(self):
        global pulse
        initLog("audiocontrol")
        pulse = pulsectl.Pulse("audiocontrol")
    
    def initcore(self, out_q, in_q):
        global queue_out, queue_in
        queue_out = out_q
        queue_in = in_q
    
    def parse(read):
        if read[0] == "conmanager": #External packet
            #Import the data. 
            data = eval(read[1][3], {'__builtins__': None}) #'{__builtins': None} so that you can't execute code. Just strings and stuff.
            external = True
            orig_device = read[1][1]
            orig_module = read[1][2]
        else: #Internal packet
            external = False
            orig_device = None
            orig_module = read[0]

        if type(read[1]) == list or type(read[1]) == tuple:
            action = read[1][0]
            params = read[1][1:]
        else:
            action = read[1][0]
            params = []
        return {"external": external, "origdevice": orig_device, "origmodule": orig_module, "action": action, "params": params}


    def respond(read, msg):
        if read[0] == "conmanager": #External packet
            #conmanager ---> audiocontrol: ("recvdata", orig_device, orig_modname, data)
            action = read[1][0]
            orig_device = read[1][1]
            orig_modname = read[1][2]
            data = read[1][2]
            if type(msg) != bytes:
                msg = bytes(msg, "utf-8")
            queue_out.put(("conmanager", ("senddata", orig_device, orig_modname, msg)))
        else: #Internal packet
            queue_out.put((read[0], (msg)))
    
    def run(self):
        global pulse
        log("running")
        time.sleep(0.05)
        if not queue_in.empty():
                read = queue_in.get()
                #External packet: ("conmanager", ("recvdata", ))
                #Internal packet:
                read = parse(read)
                if type(read[1]) == list or type(read[1]) == tuple:
                    action = read[1][0]
                else:
                    action = read[1]
                
                match action:
                    case "listsources":
                        sources = pulse.source_list()
                        senddata = ""
                        for source in sources:
                            senddata += "{}:'{}','{}','{}','{}','{}'|".format(source.index, source.description, source.mute, source.channels, source.volumes)
                        senddata = senddata[:-1]
                        respond(read, senddata)
                    case "listsinks":
                        sinks = pulse.sink_list()
                        senddata = ""
                        for sink in sinks:
                            senddata += "{}:'{}','{}','{}','{}','{}'|".format(sink.index, sink.description, sink.mute, sink.channels, sink.volumes)
                        senddata = senddata[:-1]
                        respond(read, senddata)
                    case "getdefaultsource":
                        defaultsource = pulse.server_info().default_source_name

                    case "getdefaultsink":
                        
                    case "setdefaultsource":
                        pass
                    case "setdefaultsink":
                        pass
                    case "getvolume":
                        pass
                    case "setvolume":
                        pass
                    case "incvolume":
                        pass
                    case "decvolume":
                        pass
                    case "getmute":
                        pass
                    case "setmute":
                        pass
                    case "togglemute":
                        pass
mainclass = audiocontrol()