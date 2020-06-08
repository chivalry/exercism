if (( $1 % 3 == 0 ))
then
    pling="Pling"
fi
if (( $1 % 5 == 0 ))
then
    plang="Plang"
fi
if (( $1 % 7 == 0 ))
then
    plong="Plong"
fi
res="${pling}${plang}${plong}"
if [[ -z "$res" ]]
then
    echo $1
else
    echo $res
fi
