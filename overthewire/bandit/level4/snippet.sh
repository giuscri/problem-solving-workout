for i in $(seq 0 9)
    do
        file inhere/-file0$i |
        egrep -i ascii
    done
