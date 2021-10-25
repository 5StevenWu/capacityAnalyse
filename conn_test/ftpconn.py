#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import paramiko

from stat import S_ISDIR as isdir


# from mysqlDB import MysqlDb

# sqlConn = MysqlDb()


class SftpConfig:
    def sftp_connect(self, host, port, username, password):
        # client = None
        # sftp = None
        # try:
        #    client = paramiko.Transport((host, port))
        # except Exception as error:
        #    print(error)
        # else:
        #    try:
        #        client.connect(username=username, password=password)
        #    except Exception as error:
        #        print(error)
        #    else:
        #        sftp = paramiko.SFTPClient.from_transport(client)
        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        sftp = None
        try:
            client.connect(host, port, username, password, timeout=5)
            client.connect(host, port, username=username, password=password, timeout=10, allow_agent=False,
                           look_for_keys=False)
        except Exception as error:
            print("连接失败", error)
        else:
            client.exec_command('ls -al')
            sftp = client.open_sftp()
        return client, sftp

    def disconnect(client):
        try:
            client.close()
        except Exception as error:
            print(error)

    def check_local(sftp, local):
        if not os.path.exists(local):
            try:
                os.makedirs(local)
            except IOError as err:
                print(err)

    def getFile(self, sftp, remote, local, ip, day, clist):
        try:
            result = sftp.stat(remote)
        except IOError as err:
            error = '[ERROR %s] %s: %s' % (err.errno, os.path.basename(os.path.normpath(remote)), err.strerror)
            print(error)
        else:
            if isdir(result.st_mode):
                dirname = os.path.basename(os.path.normpath(remote))
                local = os.path.join(local, dirname)
                self.check_local(local)
                for file in sftp.listdir(remote):
                    # if ('000000' not in file) and ('ericsson' in local):
                    if ('000000' not in file and 'ericsson' in local) or (
                            ('-ALLV' not in file and 'EUTRANCELLTDD' in file) or (
                            '-ALLV' not in file and 'EUTRANRELATION' in file) or (
                                    '-ALLV' not in file and 'EUTRANCELLFDD' in file) or (
                                    '-ALLV' not in file and 'EUTRANFREQRELATION' in file) or (
                                    '-ALLV' not in file and 'REPORTCONFIGA5' in file) or (
                                    '-ALLV' not in file and 'REPORTCONFIGSEARCH' in file) or (
                                    '-ALLV' not in file and 'SECTORCARRIER' in file)):
                        continue

                    if ('-ALLV' not in file) and ('huawei' in local):
                        continue
                    if ('-ALLV' not in file) and ('zte' in local):
                        continue
                    if ('-ALLV' not in file) and ('nokia' in local):
                        continue
                    if '120000.' in file:
                        continue

                    for ff in clist:
                        if ff in file:
                            sub_remote = os.path.join(remote, file)
                            sub_remote = sub_remote.replace('\\', '/')
                            self.getFile(sftp, sub_remote, local, ip, day, clist)
            else:
                if os.path.isdir(local):
                    local = os.path.join(local, ip + '-' + os.path.basename(remote))
                try:
                    sftp.get(remote, local)
                except IOError as err:
                    print(err)
                else:
                    print('[get]', local)

    def getPmFile(self, sftp, remote, local, ip, path1):
        # 检查远程文件是否存在
        try:
            result = sftp.stat(remote)
        except IOError as err:
            error = '[ERROR %s] %s: %s' % (err.errno, os.path.basename(os.path.normpath(remote)), err.strerror)
            print(error)
        else:
            if isdir(result.st_mode):
                dirname = os.path.basename(os.path.normpath(remote))
                local = os.path.join(local, dirname)
                self.check_local(local)
                for file in sftp.listdir(remote):
                    if 'EUTRANCELLNB' in file:
                        continue

                    if 'PM-ENB-EUTRANCELL' in file and path1 in file:
                        sub_remote = os.path.join(remote, file)
                        sub_remote = sub_remote.replace('\\', '/')
                        self.getPmFile(sftp, sub_remote, local, ip, path1)
                    elif 'PM-ENB-LTE-EUTRANCELL' in file and path1 in file:
                        sub_remote = os.path.join(remote, file)
                        sub_remote = sub_remote.replace('\\', '/')
                        self.getPmFile(sftp, sub_remote, local, ip, path1)
            else:
                if os.path.isdir(local):
                    local = os.path.join(local, ip + '-' + os.path.basename(remote))
                try:
                    sftp.get(remote, local)
                except IOError as err:
                    print(err)
                else:
                    print('[get]', local)

    def downNorthCmFile(self, local, day, clist, omclist, type):

        for omc in omclist:
            # username, password, host, port
            try:
                self.getFile(self.sftp_connect(username=omc[1], password=omc[2], host=omc[0], port=omc[3])[1],
                             omc[4] + type + day, omc[5] + local, omc[0], day, clist)
            except Exception as e:
                print(e)

    def downNorthPmFile(self, local, path1, omclist, type):

        for omc in omclist:
            # username, password, host, port
            try:
                self.getPmFile(self.sftp_connect(username=omc[1], password=omc[2], host=omc[0], port=omc[3])[1],
                               omc[4] + type, omc[5] + local, omc[0], path1)
            except Exception as e:
                print(e)


ftp_obj = SftpConfig()

hostdic = {'39.155.198.172': {"port": 41022, "username": 'root', "password": 'rZ@s9r'}}
if __name__ == '__main__':
    for ip, info in hostdic.items():

        client, sftp = ftp_obj.sftp_connect(ip, info.get('port'), info.get('username'), info.get('password'))
       # client.exec_command('ls -al')
        client.close()
