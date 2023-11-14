#/bin/bash

greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

ip=$(hostname -I)
file="IPs.txt"
isRepeated=false
while IFS= read -r line
do
	if [[ "$line" == "$ip" ]]; then
		isRepeated=true
		break
	fi
done < "$file"

if [ "$isRepeated" = false ]; then
	echo "$ip" >> "$file"
	echo -e "${greenColour}[+] Wifi añadida con éxito a la lista de IPs ${endColour}"
else
	echo -e "${redColour}[!] La Wifi ya ha sido añadida anteriormente${endColour}"
fi

