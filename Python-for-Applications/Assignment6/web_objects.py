class Request:
    """Represents an HTTP request. Parses a request and creates properties
    on this request instance. For example... if the request is:

    GET /dice HTTP/1.1
    User-Agent: p4a browser ftw! 
    Host: localhost:5000
    Accepts: text/html

    Then a Request object representing the above request (where req is the
    instance name):

    req.path --> "/dice"
    req.method --> "/GET"
    req.http_version --> "HTTP/1.1"
    req.headers --> {
        "User-Agent": "p4a browser ftw!",
        "Host": "localhost:5000",
        "Accepts": "text/html"
    }
    req.body --> "" (the request did not have a body)
    """
    # Based heavily on code example linked in assignment
    def __init__(self, request_text):
    	request_lines = request_text.split('\r\n')
    	parts = request_lines[0].split(' ')
    	self.method, self.path, self.http_version = parts
    	self.headers={}
    	j=1;
    	i = request_lines[j];
    	while(i != ''):
    		line = i.split(':')
    		key = line[0]
    		self.headers[key]= line[1][1:]
    		j+=1
    		i=request_lines[j]
    	self.body = request_lines[j+1]	
    def __str__(self):
    	bigString="%s %s %s" % (self.method, self.path, self.http_version)
    	for key, value in self.headers.items():
    		bigString+=("\n%s: %s" % (key, value))
    	bigString+="\n"
    	bigString+="\n%s"%(self.body)
    	return bigString

class Response:
    """An object that represents an HTTP response. Example usage:

    res = Response(200)
    res.set_header('Content-Type', 'text/html')
    res.set_header('Server', 'p4a server ftw!')
    res.set_body('<h1>stuff</h1>')
    print(res)

    # prints out...

    HTTP/1.1 200 OK
    Content-Type: text/html
    Server: p4a server ftw!

    <h1>stuff</h1>
    """

    # TODO: WRITE YOUR IMPLEMENTATION HERE!
    
    STATUS_TEXT={
    			200:'OK',
    			404:'Page not found',
    }
    
    def __init__(self, status_code):
    	self.status_code = status_code
    	self.headers={}
    	
    def set_header(self, header_name, header_value):
    	self.headers[header_name]=header_value
    def set_body(self, body):
    	self.body=body
    def set_status(self, status_code):
    	self.status_code=status_code
    
    def __str__(self):
    	bigString= "%s %s %s" % ("HTTP/1.1", self.status_code, Response.STATUS_TEXT[self.status_code])
    	for key, value in self.headers.items():
    		bigString+=("\n%s: %s" % (key, value))
    	bigString+="\n"
    	bigString+="\n%s"%(self.body)
    	return bigString

if __name__ == '__main__':
    """
    POST /stuff/add HTTP/1.1
    User-Agent: p4a browser ftw!
    Host: localhost:5000
     
    foo=bar
    """
    # PARSE A STRING INTO AN HTTP REQUEST OBJECT
    http_req = "POST /stuff/add HTTP/1.1\r\nUser-Agent: p4a browser ftw!\r\nHost: localhost:5000\r\n\r\nfoo=bar"
    req = Request(http_req)
    print(req.path)
    print(req.headers)
    print(req.body)
    print(req)
    # CREATE A RESPONSE OBJECT AND PRINT IT OUT
    res = Response(200)
    res.set_header('Content-Type', 'text/html')
    res.set_header('Server', 'p4a server ftw!')
    res.set_body('<h1>stuff</h1>')
    print(res)