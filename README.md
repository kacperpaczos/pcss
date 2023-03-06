# pcss' app

How to run this app.
Excetue in root drietory of this project:

`sudo docker compose up --build`




How it works, even connection to this app register in database, saving is date (day, months, yerar) and hours of the connection.

You can test this app:

curl -X POST -H "Content-Type: text/html" http://172.28.0.22:5000/

curl -X POST -H "Content-Type: text/yaml" http://172.28.0.22:5000/

curl -X POST -H "Content-Type: text/xml" http://172.28.0.22:5000/
curl -X POST -H "Content-Type: text/xml" -d @xmltest.xml http://172.28.0.22:5000/

curl -X POST -H "Content-Type: text/plain" http://172.28.0.22:5000/


