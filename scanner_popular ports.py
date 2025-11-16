import subprocess

# Read targets from file
with open("targets.txt", "r") as f:
    targets = [line.strip() for line in f.readlines() if line.strip()]

# List of most commonly used ports (faster than full scan)
COMMON_PORTS = [
    "21","22","23","25","53","80","110","111","123","135","139","143","161",
    "389","443","445","587","631","636","993","995","1433","1521","1723",
    "3306","3389","5432","5900","6379","8080","8081","8443","8888","9200"
]

# Convert list to Nmap format
port_string = ",".join(COMMON_PORTS)

for target_ip in targets:
    nmap_argument = ["nmap", f"-p{port_string}", target_ip]

    process = subprocess.Popen(
        nmap_argument,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    output, error = process.communicate()

    if error:
        print(f"# {error.strip()}")
        exit(1)

    open_ports = []
    for line in output.splitlines():
        if "open" in line:
            port = line.split()[0]             # "80/tcp"
            port_number = port.split("/")[0]   # "80"
            open_ports.append(port_number)

    if open_ports:
        for open_port in open_ports:
            print(f"{target_ip} Open port: {open_port}")
    else:
        print(f"{target_ip}: No open ports")
