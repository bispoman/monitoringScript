import requests
import time
import datetime
import csv
with open('bairrosReport.csv', 'w', newline='') as f:
    filewriter = csv.writer(f)
    
    filewriter.writerow(['timestamp', '2XX status count', '4XX status count', '5XX status count'])

    while True:
        startTime = time.time()
        while time.time() < startTime+60: 
            status2 = 0
            status4 = 0
            status5 = 0
            response = requests.get("https://desafioperformance.b2w.io/bairros")
            status = str(response.status_code)[:1]
            if status == 2: 
                status2 = status2 + 1
            if status == 4:
                status4 = status4 + 1
            if status == 5:
                status5 = status5 + 1
            time.sleep(2)

        if (status4 + status5) > status2:
            requests.put("https://desafioperformance.b2w.io/reinicia")
        filewriter.writerow([datetime.fromtimestamp(startTime), status2, status4, status5])