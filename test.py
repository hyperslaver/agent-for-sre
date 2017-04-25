#!/usr/bin/python3
# encoding: utf-8
import psutil,sys,datetime,re
from agent_for_sre.Collector.NetinfoProcessCollector import NetinfoProcessCollector
from agent_for_sre.Collector.FileinfoProcessCollector import FileinfoProcessCollector
from agent_for_sre.Conf.ConfAnalyzer import ConfAnalyzer
from agent_for_sre.Monitor.DnsMonitor import DnsMonitor
from agent_for_sre.Monitor.UrlMonitor import UrlMonitor

if __name__ == "__main__":
	#pinfo={ "pname" : "gorouter" }
	#henry=NetinfoProcessCollector(pinfo)
	#print(henry.get_net_listen_list('simple'))
	#henry=FileinfoProcessCollector(pinfo)
	#henry.get_file_list()
	#henry.get_logfile_list()
	#henry.print_net_est_list()
	Henry=ConfAnalyzer('./x3.yaml')
	abc=Henry.getMonitorMonitorlistByProduct('cia')
	test=Henry.getMonitorDevicelistByProduct('cia')
	tmp=[]
	for i in test:
		for ip in i['ips']:
			for item in i['monitor_items']:
				tmp.append({'ip':ip,'define':abc[item]})
	for i in tmp:
		if(i['define']['function']=='url_check'):
			checker1=UrlMonitor(i['ip'],i['define'])
			for data1 in checker1.url_check():
				print(data1)
		if(i['define']['function']=='dns_resolve_check'):
			checker2=DnsMonitor(i['ip'],i['define'])
			for data2 in checker2.dns_resolve_check():
				print(data2)
