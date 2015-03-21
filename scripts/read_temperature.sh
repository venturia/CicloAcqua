#!/bin/bash

term=/sys/bus/w1/devices/$1
if [ -d  "$term" ]; then
  result=`cat $term/w1_slave`
  if [[ "$result" == *"YES"* ]]; then
    temp=`echo ${result/*t=/} | awk '{print $1/1000.}'`
    echo $temp
  else
    echo "Errore" 
  fi
else
  echo "Non esiste"
fi
