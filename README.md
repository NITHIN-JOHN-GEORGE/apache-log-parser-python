As part of this **DevOps project**, we showcase how Python scripting can be used to parse Apache access logs in real-world scenarios. Two years ago, I posted a shell script ([https://github.com/NITHIN-JOHN-GEORGE/apache_log_parser](https://github.com/NITHIN-JOHN-GEORGE/apache_log_parser)) for performing this operation. The following is a Python implementation of the same.

## Concepts in Python used in this Project:

- Regex with re module
- Argparser Module
- Functions
- OS module
- sys module
- csv and datetime module
- Counter from Collection Module
- Loops
- Conditional Statements

### About The Project

The script allows users to analyze and extract specific data from Apache access log files. The Apache access log file is a text file that contains information about requests made to the Apache webserver. This information includes details such as the IP address of the client making the request, the request method used, the time and date of the request, the requested URL, and the HTTP status code returned by the server.

The script accepts user input parameters, including the location of the Apache access log file to parse, the type of operation to perform, and the output format of the result (either table or CSV). It uses the argparse module to parse user input parameters.

The script is designed to accept three user input parameters:

- the location of the Apache access log file to parse
- the type of operation to perform.
- and the output format of the result (either table or CSV)

The script can perform four types of operations. 

- First, it can count the most frequently visited IP addresses, returning the IP addresses with the highest number of hits. The script uses regular expressions to extract IP addresses from the log file and the Counter module to count the number of occurrences of each IP address.
- Second, it can count the number of times each request method (GET, POST, PUT, or DELETE) appears in the log file and returns the methods with the highest number of hits.
- Third, it can count the number of times each base URL (the part of the URL before the query string) appears in the log file and returns the URLs with the highest number of hits. The script uses regular expressions to extract base URLs from the log file and the Counter module to count the number of occurrences of each base URL.
- Finally, it can count the number of times each HTTP status code appears in the log file and returns the codes with the highest number of hits.

The script uses regular expressions to extract the relevant data from the log file and the Counter module to count the number of occurrences of each data point. It also includes helper functions for checking if the log file exists and for printing headers and centering text.The script uses the os and datetime modules to generate timestamps and get the size of the terminal window.

Once the script has performed the requested operation, it outputs the results either to the console or a CSV file, depending on the user's specified output format. If the output format is "table," the script formats the output as a table using the print function. If the output format is "CSV," the script writes the output to a CSV file using the csv module.
