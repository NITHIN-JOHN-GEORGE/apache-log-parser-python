import re
import os
import sys
import csv
import datetime
from collections import Counter
import argparse

# Author : NITHIN JOHN GEORGE 

def print_header():
    print("\n" + "#" * os.get_terminal_size().columns + "\n")


def center(message):
    col = os.get_terminal_size().columns
    pre_space = (col - len(message)) // 2
    print_header()
    print(" " * pre_space + message)
    print_header()

def file_exists(filename):
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        sys.exit(1)

def most_visited_ips(logfile, output_format):

    file_exists(logfile.name)
    
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    

    with open(logfile.name) as f:
        log_file = f.read()
        ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log_file)
        ips_counted = Counter(ips)
        ips_sorted = ips_counted.most_common()

    if output_format == 'csv':
        csv_filename=f"most_visited_ip_{now}.csv"
        with open(csv_filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['IP_ADDRESS', 'NO_OF_TIMES_ACCESSED'])
            for ip, count in ips_sorted:
                writer.writerow([ip, count])
    elif output_format == 'table':
        center("Welcome to Apache Log Parser : ")
        center("Most Accessed IPs With Count")
        print("\n{:<20} {:<20}".format('IP_ADDRESS', 'NO_OF_TIMES_ACCESSED'))
        header = "{:<20} {:<20}".format('IP_ADDRESS', 'NO_OF_TIMES_ACCESSED')
        print("-" * len(header))
        print("\n")
        for ip, count in ips_sorted:
            print("{:<20} {:<20}".format(ip, count))
        print_header()
    else:
        print("Invalid output format specified. Please choose either 'csv' or 'table'")



def count_request_methods(logfile, output_format):

    file_exists(logfile.name)
    
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    with open(logfile.name) as f:
        requests = re.findall(r'"(GET|POST|PUT|DELETE)', f.read())
        request_counts  = Counter(requests)
        top_requests  = request_counts.most_common(20)

    if output_format == 'csv':
        csv_filename=f"top_request_methods_{now}.csv"
        if os.path.exists(csv_filename):
            os.remove(csv_filename)
        with open(csv_filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['REQUEST_METHOD', 'COUNT'])
            for request, count in top_requests:
                writer.writerow([request, count])
    elif output_format == 'table':
          center("Welcome to Apache Log Parser : ")
          center("Top Request Methods With Count")
          print("\n{:<20} {:<20}".format('REQUEST METHOD', 'COUNT'))
          print("{:<20} {:<20}".format('==============', '====='))
          print("\n")
          for request, count in top_requests:
               print("{:<20} {:<20}".format(request, count))
          print_header()
    else:
        print("Invalid output format specified. Please choose either 'csv' or 'table'")


def get_top_urls(logfile, output_format):


    file_exists(logfile.name)

    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    with open(logfile.name) as f:
        requests = re.findall(r'"(GET|POST|PUT|DELETE)\s(\S+)', f.read())
        url_counts  = Counter(requests)
        top_urls  = url_counts.most_common(20)

    if output_format == 'csv':
        csv_filename=f"top_base_urls_{now}.csv"
        if os.path.exists(csv_filename):
            os.remove(csv_filename)
        with open(csv_filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['REQUEST_METHOD', 'BASE_URL' , 'COUNT'])
            for url, count in top_urls:
                method, base_url = url
                writer.writerow([method,  base_url, count])
    elif output_format == 'table':
        center("Welcome to Apache Log Parser : ")
        center("Top Hitted 20 Base URL With Count")
        print("\n{:<20} {:<20} {:<20}".format('REQUEST METHOD', 'BASE_URL','COUNT'))
        print("{:<20} {:<20} {:<20}".format( '==============',  '========','====='))
        print("\n")
        for url, count in top_urls:
            method, base_url = url
            print("{:<20} {:<20} {:<20}".format(method, base_url, count))
        print_header()
    else:
        print("Invalid output format specified. Please choose either 'csv' or 'table'")

def count_status_code(logfile , output_format):
    
    file_exists(logfile.name)

    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    with open(logfile.name) as f:
        codes = re.findall(r'\s(\d{3})\s', f.read())
        code_counts   = Counter(codes)
        sorted_codes  = code_counts.most_common(20)

    if output_format == 'csv':
        csv_filename=f"top_http_status_codes_{now}.csv"
        if os.path.exists(csv_filename):
            os.remove(csv_filename)
        with open(csv_filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['HTTP_STATUS_CODE', 'COUNT'])
            for code, count in sorted_codes:
                writer.writerow([code, count])
    elif output_format == 'table':
        center("Welcome to Apache Log Parser : ")
        center("Top HTTP Status Code With Count")
        print("\n{:<20} {:<20}".format('HTTP STATUS CODE', 'COUNT'))
        print("{:<20} {:<20}".format('==================', '====='))
        print("\n")
        for code, count in sorted_codes:
            print("{:<20} {:<20}".format(code, count))
        print_header()
    else:
        print("Invalid output format specified. Please choose either 'csv' or 'table'")


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Apache Access Log Parser", formatter_class=argparse.RawTextHelpFormatter) 

    parser.add_argument("-l", "--logfile", help='Path to Apache access log file to parse',
                        dest="logfile", type=argparse.FileType('r'), required=True)

    parser.add_argument("-o", "--operation", help='\nChoose from one of the following operations to perform on the log data:\n'
                                            ' \n - "most-visited-ips" - count most frequently visited IP addresses\n'
                                              '  - "top-request-methods" - count most frequently used request methods\n'
                                              '  - "top-base-urls" - count most frequently hit base URLs\n'
                                              '  - "top-http-status-codes" - count most frequent HTTP status codes',
                    dest="operation", type=str, choices=['most-visited-ips', 'top-request-methods', 'top-base-urls' , 'top-http-status-codes'] , required=True)

    
    parser.add_argument("-f", "--output-format", help='Please enter the output format: ',
                        dest="output_format", type=str, choices=['table', 'csv'], required=True)


    args = parser.parse_args()
    
    
    if args.operation == 'most-visited-ips':
        most_visited_ips(args.logfile, args.output_format)
    elif args.operation == 'top-request-methods':
        count_request_methods(args.logfile ,args.output_format)
    elif args.operation == 'top-base-urls':
        get_top_urls(args.logfile , args.output_format)
    elif args.operation == 'top-http-status-codes':
        count_status_code(args.logfile , args.output_format)
    else:
        print("Invalid operation specified. Please choose either 'most-visited-ips', 'top-request-methods', 'top-base-urls' or 'top-http-status-codes'")
