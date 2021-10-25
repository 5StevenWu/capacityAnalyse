import paramiko


def sftpconn():
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect('39.155.198.172', 41022, username='root', password='rZ@s9r', timeout=5)

    stdin, stdout, stderr = client.exec_command('ls -l')

    for std in stdout.readlines():
        print(std)


def sftpconn2(ip, port, username, password):
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # client.connect('39.155.198.172', 41022, username='root', password='rZ@s9r', timeout=5)
    client.connect(ip, port, username, password, timeout=5)
    stdin, stdout, stderr = client.exec_command('ls -l')

    for std in stdout.readlines():
        print(std)


if __name__ == '__main__':
   # sftpconn()
   sftpconn2('39.155.198.172', 41022, 'root', 'rZ@s9r')
