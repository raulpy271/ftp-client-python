import ftplib

os = input('Qual sistema operacional vc quer saber a versão mais recente? \n')

# Fill Required Information
HOSTNAME = "ftp.fau.de"
 
# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME)

login_response = ftp_server.login()

print(f"Response: {login_response}")

if os == 'fedora':
    path = '/fedora/linux/releases/'
elif os == 'mint':
    path = '/mint/iso/stable/'
else:
    raise Exception('O sistema operacional escolhido ainda não estar disponível')

ftp_server.cwd(path)

listDir = ftp_server.nlst()

listDir = list(filter(lambda dir: dir.replace('.', '').isdecimal(), listDir))

versionsFloat = list(map(float, listDir))

versionsFloat.sort(reverse=True)

print(f'A versao mais recente do {os} é: {versionsFloat[0]}')

ftp_server.quit()
