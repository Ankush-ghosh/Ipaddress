#By Drop.org.in Contact us for more info
import pygeoip

gip=pygeoip.GeoIP("GeoLiteCity.dat")
res=gip.record_by_addr('1.39.255.255')
for key,val in res.items():
    print("%s : %s"%(key,val))
#By Drop.org.in Contact us for more info
