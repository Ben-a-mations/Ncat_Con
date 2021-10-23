printf "#!/bin/bash\ncd\ncd Ncat_Con && ./man.sh && cd" > netcon
chmod +x netcon
sudo cp netcon /usr/bin/
rm -rf netcon