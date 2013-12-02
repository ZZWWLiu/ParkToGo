#!/usr/bin/env python

import json, urllib, urllib2, socket
import re


class IPInfo() :
    def __init__(self, apikey) :
        self.apikey = apikey
    def GetPublicIp(self):
        u = 'http://checkip.dyndns.org/'
        q_obj = urllib2.urlopen(u)
        ip_text = q_obj.read()
        pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
        ip = re.findall(pattern, ip_text)
        return ip[0][0]

    def GetIPInfo(self, baseurl, ip=None, timezone=False) :
        """Same as GetCity and GetCountry, but a baseurl is required.  
        This is for if you want to use a different server that uses the the php scripts on ipinfodb.com."""
        passdict = {"key":self.apikey, "format": "json"}
        if ip :
            try:
                passdict["ip"] = socket.gethostbyaddr(ip)[2][0]
            except : 
                passdict["ip"] = ip
        else:
            passdict["ip"] = self.GetPublicIp()
            # print ip[0][0]
        if timezone :
            passdict["timezone"] = "true"
        else :
            passdict["timezone"] = "false"
        urldata = urllib.urlencode(passdict)
        # print urldata
        url = baseurl + urldata
        urlobj = urllib2.urlopen(url)
        data = urlobj.read()
        urlobj.close()
        datadict = json.loads(data)
        return datadict

    def GetCity(self, ip=None, timezone=False) :
        """Gets the location with the context of the city of the given IP.  
        If no IP is given, then the location of the client is given.  
        The timezone option defaults to False, to spare the server some queries."""

        # baseurl = "http://api.ipinfodb.com/v2/ip_query.php"
        baseurl = "http://api.ipinfodb.com/v3/ip-city/?"
        return self.GetIPInfo(baseurl, ip, timezone)

    def GetCountry(self, ip=None, timezone=False) :
        """Gets the location with the context of the country of the given IP.  If no IP is given, then the location of the client is given.  The timezone option defaults to False, to spare the server some queries."""
        baseurl = "http://api.ipinfodb.com/v2/ip_query_country.php"
        return self.GetIPInfo(baseurl, ip, timezone)

if __name__ == "__main__":
    ipinfo = IPInfo('97f4d203b989b3fe87045b255e7a29d42f403cafc8726c45172079dbaa60fbfe')
    print ipinfo.GetCity()
