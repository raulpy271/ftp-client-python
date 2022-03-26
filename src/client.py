import ftplib

def obtem_versoes(ftp_client, os):
    if os == 'fedora':
        path = '/fedora/linux/releases/'
    elif os == 'mint':
        path = '/mint/iso/stable/'
    else:
        raise Exception('O sistema operacional escolhido ainda não estar disponível')

    ftp_client.cwd(path)

    list_dir = ftp_client.nlst()

    return list_dir

def parse_versoes(list_dir):
    list_dir = list(filter(lambda dir: dir.replace('.', '').isdecimal(), list_dir))

    versions_float = list(map(float, list_dir))

    return versions_float

def obtem_versao_recente(versoes):
    versoes_float = parse_versoes(versoes)
    versoes_float.sort(reverse=True)
    return versoes_float[0]

if __name__ == '__main__':
    os = input('Qual sistema operacional vc quer saber a versão mais recente? \n')
    HOSTNAME = "ftp.fau.de"
    ftp_client = ftplib.FTP(HOSTNAME)
    login_response = ftp_client.login()
    print(f"Response: {login_response}")
    versoes = obtem_versoes(ftp_client, os)
    mais_recente = obtem_versao_recente(versoes)
    print(f'A versao mais recente do {os} é: {mais_recente}')
    ftp_client.quit()

