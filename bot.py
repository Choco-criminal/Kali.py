import os  
import subprocess  
  
# Update and upgrade the system  
subprocess.run(['apt-get', 'update', '-y'])  
subprocess.run(['apt-get', 'upgrade', '-y'])  
subprocess.run(['apt-get', 'install', '-y', 'sudo'])  
  
# Install required packages  
subprocess.run(['sudo', 'apt-get', 'install', '-y', 'curl', 'ffmpeg', 'git', 'locales', 'nano', 'python3-pip', 'screen', 'ssh', 'unzip', 'wget'])  
  
# Set locale  
subprocess.run(['localedef', '-i', 'en_US', '-c', '-f', 'UTF-8', '-A', '/usr/share/locale/locale.alias', 'en_US.UTF-8'])  
  
# Install Node.js  
subprocess.run(['curl', '-sL', 'https://deb.nodesource.com/setup_21.x', '|', 'bash', '-'])  
subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nodejs'])  
  
# Set environment variables  
os.environ['LANG'] = 'en_US.utf8'  
ngrok_token = '2oGnoXbY0Qh54bNrgEmUgqaQhTp_yRNTtHpDahH8YDP7xWjr'  
  
# Download and install ngrok  
subprocess.run(['wget', '-O', 'ngrok.zip', 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.zip'])  
subprocess.run(['unzip', 'ngrok.zip'])  
  
# Configure ngrok  
with open('/start', 'a') as f:  
   f.write('./ngrok config add-authtoken {}\n'.format(ngrok_token))  
   f.write('./ngrok tcp --region ap 22 &>/dev/null &\n')  
  
# Configure SSH  
subprocess.run(['mkdir', '/run/sshd'])  
with open('/start', 'a') as f:  
   f.write('/usr/sbin/sshd -D\n')  
with open('/etc/ssh/sshd_config', 'a') as f:  
   f.write('PermitRootLogin yes\n')  
   f.write('PasswordAuthentication yes\n')  
subprocess.run(['echo', 'root:kaal', '|', 'chpasswd'])  
subprocess.run(['service', 'ssh', 'start'])  
  
# Make the /start script executable  
subprocess.run(['chmod', '755', '/start'])  
  
# Expose ports  
subprocess.run(['EXPOSE', '80', '8888', '8080', '443', '5130', '5131', '5132', '5133', '5134', '5135', '3306'])  
  
# Run the /start script  
subprocess.run(['/start'])
