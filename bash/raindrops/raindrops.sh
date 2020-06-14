#!/usr/bin/env bash

res=""
(( $1 % 3 == 0 )) && res="Pling"
(( $1 % 5 == 0 )) && res+="Plang"
(( $1 % 7 == 0 )) && res+="Plong"
if [[ -z "$res" ]]
then
    echo "$1"
else
    echo "$res"
fi
