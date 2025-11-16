import subprocess
import socket

def load_targets(filename="targets.txt"):
    targets = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            targets.append(line)
    return targets


def scan_target(target):
    try:
        resolved_ip = socket.gethostbyname(target)
        print(f"\nScanning {target} ({resolved_ip}) ...")
    except socket.gaierror:
        print(f"[!] Cannot resolve {target}")
        return

    args = ["nmap", "-T4", "-p-", target]  # Fast, full port scan
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate()

    if error.strip():
        print(f"ERROR: {error.strip()}")

    open_ports = []

    for line in output.splitlines():
        if "open" in line and "/tcp" in line:
            port = line.split()[0]
            port_number = port.split("/")[0]
            open_ports.append(port_number)

    if open_ports:
        for p in open_ports:
            print(f"[+] {target} open port: {p}")
    else:
        print(f"[-] No open ports found on {target}")


if __name__ == "__main__":
    print("=== Python Port Scanner ===")
    targets = load_targets()

    print(f"Loaded {len(targets)} targets:")
    for t in targets:
        print(f" - {t}")

    print("\nStarting scan...")

    for target in targets:
        scan_target(target)

    print("\n=== Scan Finished ===")
