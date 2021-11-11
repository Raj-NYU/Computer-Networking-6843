Lab 2: Web Server Lab
 
In this lab, you will learn the basics of socket programming for TCP connections in Python: how to create a socket, bind it to a specific address and port, and send and receive a HTTP packet. You will also learn some basics of HTTP header format.
 
You will develop a web server that handles one HTTP request at a time. Your web server should accept and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response message consisting of the requested file preceded by header lines, and send the response directly to the client. If the requested file is not present in the server, the server should send an HTTP “404 Not Found” message back to the client.
 
 
Running the Server
Put an HTML file (e.g., helloworld.html) in the same directory that the server is in. Run the server program. Determine the IP address of the host that is running the server (e.g., 127.0.0.1). Open a browser and provide the corresponding URL. For example:
http://127.0.0.1:13331/helloworld.html
 
‘helloworld.html’ is the name of the file you placed in the server directory. Note also the use of the port number after the colon. GradeScope will test your code using port 13331. In the above example, we have used the port number 13331. The browser should then display the contents of helloworld.html. If you omit ":13331", the browser will assume port 80 and you will get the web page from the server only if your server is listening at port 80. Next, try to get a file that is not present at the server. You should get a “404 Not Found” message.
