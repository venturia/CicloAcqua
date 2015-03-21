#!/usr/bin/python

import time
import datetime
import subprocess

time_interval=10
outfilename="/home/pi/CicloAcqua/temperature.out"
termometri=[]
termometri.append(["28-00000595887c","Freddo"])
termometri.append(["28-0000059553da","Caldo"])

while True:
   outfile=open(outfilename,"w")
   data=str(datetime.datetime.now())
   outfile.write(data)
   outfile.write("<br>\n")
   for termometro in termometri:
      command="/home/pi/CicloAcqua/scripts/read_temperature.sh"
      temp=subprocess.check_output([command,termometro[0]])
      outfile.write("<font size='6'>")
      outfile.write(termometro[1])
      outfile.write(" ")
      outfile.write(temp)
      outfile.write("</font><br>")
   outfile.close()
   time.sleep(time_interval)





