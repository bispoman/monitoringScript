# monitoringScript
A simple Python script to monitor a given URL and write a report on a CSV file.

This script was written using Python 3.7.4 and as is, monitors the URL: https://desafioperformance.b2w.io/bairros

Every two seconds it makes a request to the URL above and after a full minute, a line will be written on the CSV file containing the timestamp, the count of 2xx responses, the count of 4xx responses and the count of 5xx responses. 
If by the end of said minute the count of 4xx and 5xx is greater than the count of 2xx, the script will make a request to https://desafioperformance.b2w.io/reinicia to try to reset the service and bring it back online. 


To run this script you'll need the following dependencies: 
requests
time
datetime
csv

All of them can be installed via PIP or your favorite package manager.

In case of any doubt, feel free to submit it as an issue. 

Thanks
