#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.extend("dns") # this line will add d, n, and s
print(proto)
# this section will remove dns and add sip to the list
proto.remove(dns)
proto.append("sip")
print proto


