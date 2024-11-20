import subprocess, re, getpass

userName = getpass.getuser()

#? I wish this worked so bad, but it downloads as 'download?platform=linux&format=deb' UmU
# subprocess.run(['wget', 'https://discord.com/api/download?platform=linux&format=deb', '-P', f'/home/{userName}/Downloads'])

process = subprocess.Popen(['ls', '-l', '-a', '-1', f'/home/{userName}/Downloads'], stdout=subprocess.PIPE); out = process.communicate()

print(out); print(type(out))

list_files = str(out)
print(list_files, type(list_files))

dc_regex = 'discord\W\d+\.\d+\.\d+\.deb'

res = re.findall(dc_regex, list_files); res.sort()
if res != []:
    print(res); latest_version = res[-1]
print(latest_version)

#! All commands to update :3c
subprocess.run(['sudo', 'dpkg', '-i', latest_version])
subprocess.run(['h', '-c' '"$(curl -sS https://raw.githubusercontent.com/Vendicated/VencordInstaller/main/install.sh)"'])
