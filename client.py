import ftplib
 
# Fill Required Information
HOSTNAME = "ftp.uem.br"
 
# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME)
 
# force UTF-8 encoding
ftp_server.encoding = "utf-8"
 
# Enter File Name with Extension
filename = "favicon.ico"
 
# Write file in binary mode
with open(filename, "wb") as file:
    # Command for Downloading the file "RETR filename"
    ftp_server.retrbinary(f"RETR {filename}", file.write)
 
# Get list of files
ftp_server.dir()
 
# Display the content of downloaded file
file= open(filename, "r")
print('File Content:', file.read())
 
# Close the Connection
ftp_server.quit()
