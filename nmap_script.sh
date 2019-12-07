nmap -sV -sC -p- --min-rate 1000 --max-retries 5 -Pn $1 -oN nmap-$1
