#!/bin/env python
#encoding=utf8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')    

import urllib
import json

class GeoCity:
    """
    Geo fetch data from www.weather.com.cn
    """
    def fetchRank2(self,id):
        """
        fetch city data
        http://sd.weather.com.cn/data/city3jdata/provshi/10101.html
        id:[1,2,...,34]
        """
        data = []
        url = "http://sd.weather.com.cn/data/city3jdata/provshi/101%s.html" % id
        j = self.fetchJson(url)
        for k,v in j.items():
            data.append((id,k,v))
            data.extend(self._fetchRank3(id,k))
        return data

    def _fetchRank3(self,id,id2):
        """
        fetch county data
        http://sd.weather.com.cn/data/city3jdata/station/1010510.html
        id:[1,2,3,...,34]
        id2:[...]
        """
        data = []
        url = "http://sd.weather.com.cn/data/city3jdata/station/101%s%s.html" % (id,id2)
        j = self.fetchJson(url)
        for k,v in j.items():
            data.append((id,id2,k,v))
        return data

    def fetchUrl(self,url):
        return urllib.urlopen(url).read()

    def fetchJson(self,url):
        return json.loads(self.fetchUrl(url))

def main():
    g = GeoCity()
    for j in ["%02d"%i for i in range(1,35)]:
        for l in [list(k) for k in g.fetchRank2(j)]:
            print "\t".join(l)

if __name__ == "__main__":
    main()
