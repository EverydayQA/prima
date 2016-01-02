#!/bin/bash

string="Le #cerveau d’#Einstein n’est « #Ordre des #Mopses\" » pas"
echo $string

echo "*** start"
# switch -o only output the matching part 
result=`echo $string| grep -o '#[[:alpha:]]*'`
echo "result:"
echo $result


echo "*** start"
# replalce all words do not start with # by a space
# remove the first word
# compact the spaces
step1=`echo $string |sed -e 's/[^[:alpha:]#][[:alpha:]]*/ /g'`
echo $step1

step2=`echo $step1|sed -e 's/^[^#]*//'`
echo $step2

step3=`echo $step2|sed -e 's/  */ /g'`
echo $step3

echo "*** start"
#{:CLASS:] character class - alnum alpha ascii blank cntrl digit lower print punct space upper word or xdigit
# replace all the matches //
step1=${string//#/ #}
echo $step1

# split space
arr=(${step1// / })
for j in ${arr[*]};
do 
    init=${j:0:1}
    last=${j:-1:1}

    if [[ ${j:0:1} == '#' ]]
    then
        z=${j//[![:alnum:]]/ }
        echo $z        
    fi

done

