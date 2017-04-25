#!/usr/bin/python3
# encoding: utf-8
import psutil,sys,datetime,re
from agent_for_sre.Collector.NetinfoProcessCollector import NetinfoProcessCollector
from agent_for_sre.Collector.FileinfoProcessCollector import FileinfoProcessCollector
from agent_for_sre.Conf.ConfAnalyzer import ConfAnalyzer
from agent_for_sre.Monitor.DnsMonitor import DnsMonitor
from agent_for_sre.Monitor.UrlMonitor import UrlMonitor

if __name__ == "__main__":
	config=ConfAnalyzer('./x3.yaml')
	monitor_list=config.getMonitorMonitorlistByProduct('cia')
	device_list=config.getMonitorDevicelistByProduct('cia')
	tmp=[]
	for device in device_list:
		for ip in device['ips']:
			for item in device['monitor_items']:
				tmp.append({'ip':ip,'define':monitor_list[item]})
	for i in tmp:
		if(i['define']['function']=='url_check'):
			checker1=UrlMonitor(i['ip'],i['define'])
			for data1 in checker1.url_check():
				print(data1)
		if(i['define']['function']=='dns_resolve_check'):
			checker2=DnsMonitor(i['ip'],i['define'])
			for data2 in checker2.dns_resolve_check():
				print(data2)
