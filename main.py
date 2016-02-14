import os, json
from threading import Thread
from Queue import Queue

host_list = {
	"Server A":"192.168.0.1",
	"Server B":"192.168.0.2"
	"Host 1":"192.168.0.100",
	"Host 2":"192.168.0.101",
	"Host 3":"192.168.0.102"
}

host_status = dict.fromkeys(host_list, 0)

queue = Queue()
map(lambda x: queue.put(x), host_list.values())

def check_host():
	while not queue.empty():
		target = queue.get()
		response = os.system("ping -c 1 -w1 " + target + " > /dev/null 2>&1")
		if response == 0:
			key = host_list.keys()[host_list.values().index(target)]
  			host_status[key] = 1

def output_json(host_status):
	return json.dumps(host_status)

def start():
	NUM_THREADS = len(host_list)
	threads = map(lambda i: Thread(target=check_host), xrange(NUM_THREADS))
	map(lambda th: th.start(), threads)
	map(lambda th: th.join(), threads)

start()
print output_json(host_status)
