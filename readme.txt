1. Backend uses Python3 and pymysql. Install both in Linux like Ubuntu and launch ServerMain.py with port 8000
2. Frontend in Booking/UI/. It uses AngularJS and AngularJS scripts have already been included. Please install apache2 on same host with backend and copy the "app" folder to /var/www/html/.
3. deploy mysql to linux machine locally, import the dump in booking\db.sql
4. Open browser, go to http://hostname/app/index.html

test team leader: Jim, password is jim123. He can update tickets in his team
global admin: Jessica, password is jessica123, she can see tickets from all teams
team member: Tom, password is tom123, he can only see tickets in his team

others: please see dbo.Users table, password is always lowercase the username + string "123"

DB is intialized as preview environment so you can control the date in dbo.SystemConfiugrations and test the rule that team leader cannot modify ticket number after 5h
