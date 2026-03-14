# DINDOOR WATCHDOG v2.0 - AI & Statistics
# Evolution: Von einfacher IP-Prüfung zu gewichtetem Risk-Scoring

def predict_threat(ip, is_vpn, cpu, p_size):
    score = 0
    # Blacklist (Altbewährt)
    malicious_ips = ["45.143.203.14", "185.220.101.34"]
    if ip in malicious_ips: score += 100
    
    # Neue KI-Kriterien (Weighted Scoring)
    if is_vpn == "True": score += 30
    if int(cpu) > 80: score += 50
    if int(p_size) > 1500: score += 20
    return score

def run_scanner():
    print("--- DINDOOR WATCHDOG v2.0 ACTIVE ---")
    total_checks = 0
    blocked_count = 0
    
    try:
        # Wir greifen auf die traffic.log im gleichen Ordner zu
        with open("src/traffic.log", "r") as log_file, open("security_report_v2.txt", "w") as report:
            report.write("--- DINDOOR SECURITY AUDIT REPORT V2 ---\n\n")
            
            for line in log_file:
                parts = line.strip().split(",")
                if len(parts) < 4: continue
                
                total_checks += 1
                ip, is_vpn, cpu, p_size = parts
                score = predict_threat(ip, is_vpn, cpu, p_size)
                
                status = "🔴 BLOCK" if score >= 70 else "🟢 ALLOW"
                if score >= 70: blocked_count += 1
                
                output = f"Score: {score:3}/100 | Status: {status} | IP: {ip}"
                print(output)
                report.write(output + "\n")
            
            # Die wissenschaftliche Auswertung
            threat_rate = (blocked_count / total_checks) * 100 if total_checks > 0 else 0
            summary = (
                f"\n--- FINAL STATISTICS ---\n"
                f"Total Analyzed: {total_checks}\n"
                f"Threats Blocked: {blocked_count}\n"
                f"Threat Detection Rate: {threat_rate:.2f}%\n"
            )
            print(summary)
            report.write(summary)
            
    except FileNotFoundError:
        print("[ERROR] Datei nicht gefunden! Prüfe den Pfad zu 'traffic.log'.")

if __name__ == "__main__":
    run_scanner()
