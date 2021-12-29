#!/bin/bash

while ((1==1))
  do

      i=1
      e=1
      s=1
        while [ $i -le 5 ]
        do
          ((i++))
          echo $i
          curl  http://192.168.1.1:80
      	  if [ $? -ne 0 ]
      	    then
      		    echo "ip1 не доступен `date +"%d-%m-%Y-%H-%M-%S"`" > ip.log
      		    exit
      		  else
      		  echo "ip1 доступен `date +"%d-%m-%Y-%H-%M-%S"`" > ip.log
      		   while [ $e -le 5 ]
              do
                ((e++))
                echo $e
                curl  http://192.168.0.1:80
                if [ $? -ne 0 ]
                  then
              	    echo "ip2 не доступен `date +"%d-%m-%Y-%H-%M-%S"`" > ip.log
              	    exit
              	  else
              	  echo "ip2 доступен `date +"%d-%m-%Y-%H-%M-%S"`" > ip.log
              	  while [ $s -le 5 ]
                    do
                      ((s++))
                      echo $s
                      curl  http://192.168.1.1:80
                      if [ $? -ne 0 ]
                        then
                    	    echo "ip3 не доступен `date +"%d-%m-%Y-%H-%M-%S"`" > ip.log
                    	    exit
                    	  else
                    	  echo "ip3 доступен `date +"%d-%m-%Y-%H-%M-%S"`" > ip.log
                      fi
                    done
                fi
              done
      	  fi
      	done
  done

