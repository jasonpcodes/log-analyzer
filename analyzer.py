def analyze_log(file_path):
    failed_attempts = {}
    with open (file_path, 'r') as file:
        for line in file:
            if "Failed login from" in line:
                parts = line.split()
                ip = parts[-1]

                if ip in failed_attempts:
                    failed_attempts[ip] += 1
                else:
                    failed_attempts[ip] = 1
    print ("\nFailed Login Summary:")

    for ip, count in failed_attempts.items():
        print(ip, ":", count, "failed logins")

analyze_log("logs/sample_log.txt")