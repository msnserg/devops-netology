#!/bin/bash
while ((1==1))
		do
			curl https://localhost:4758
			if (($? != 1))
			then
			date > "`date +"%d-%m-%Y"`".log
			fi
		done