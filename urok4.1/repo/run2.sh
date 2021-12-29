#!/bin/bash
i=1
  while [ $i -le 5 ]
	do
	  ((i++))
	  curl  http://192.168.1.1:80
	  if [ $? -ne 0 ]
	    then
	      echo "ip1 не доступен `date +"%d-%m-%Y-%H-%M-%S"`" > ip1.log
	    else
	    echo "ip1 доступен `date +"%d-%m-%Y-%H-%M-%S"`" > ip1.log
	  fi
	done

