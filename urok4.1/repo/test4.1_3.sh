#!/bin/bash
ip=( "http://192.168.1.1:80" "http://192.168.1.0:80" "http://192.168.1.1:80")
i=1
  while [ $i -le 5 ]
	do
	  ((i++))
    for a in ${ip[@]}
    do
      curl  $a
      if [ $? -ne 0 ]
	      then
	        echo $a "ip не доступен `date +"%d-%m-%Y-%H-%M-%S"`" >> ip_err.log
	        exit
	      else
	      echo $a "ip доступен `date +"%d-%m-%Y-%H-%M-%S"`" >> ip_err.log
	    fi
	  done
	done