import argparse
from fim import baseline, monitor, checker

def main():
    parser = argparse.ArgumentParser(
        description="🛡️ Custom File Integrity Monitoring (FIM) Tool"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # baseline command
    parser_baseline = subparsers.add_parser("baseline", help="Generate file baseline")
    parser_baseline.add_argument("directory", help="Directory to baseline")

    # monitor command
    parser_monitor = subparsers.add_parser("monitor", help="Start real-time monitoring")
    parser_monitor.add_argument("directory", help="Directory to monitor")

    # check command
    parser_check = subparsers.add_parser("check", help="Check integrity against baseline")
    parser_check.add_argument("directory", help="Directory to check")

    args = parser.parse_args()

    if args.command == "baseline":
        baseline.generate_baseline(args.directory)
    elif args.command == "monitor":
        monitor.start_monitoring(args.directory)
    elif args.command == "check":
        checker.check_integrity(args.directory)
