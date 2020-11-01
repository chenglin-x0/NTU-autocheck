# NTU-autocheck
RA autocheck for NTU.

With Linux and Anaconda.

crontab setting:
m  h  dom mon   dow       command
20 17  *   *   1,2,3,4,5  /home/local_username/anaconda3/bin/python /home/local_username/Desktop/RACHECK/signout.py >/home/local_username/Desktop/RACHECK/checkout.log 2>&1
01 08  *   *   1,2,3,4,5  /home/local_username/anaconda3/bin/python /home/local_username/Desktop/RACHECK/signin.py  >/home/local_username/Desktop/RACHECK/checkin.log 2>&1

