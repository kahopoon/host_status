# host_status
check list of hosts, return up/down status in json format by stdout.

multi threads on ping requests for instant result

# Example

Server A, Host 1 Up

Server B, Host 2, Host 3 Down

python main.py

{"Server A": 1, "Server B": 0, "Host 1": 1, "Host 2": 0, "Host 3": 0}
