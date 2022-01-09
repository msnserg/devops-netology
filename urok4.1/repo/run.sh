#!/bin/bash
while ((1==1))
  do
		curl http://192.168.1.1:80
		#echo $?
		if (($? != 0))
		then
		  date > "`date +"%d-%m-%Y"`".log
		  continue
		else
		  echo "Сервис доступен `date +"%d-%m-%Y-%H-%M-%S"`" >> "`date +"%d-%m-%Y"`".log
		  exit
		fi
	done