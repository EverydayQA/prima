
#!/bin/bash
echo "what is your first number?";
read number1
echo "what is your second number?";
read number2
for i in $(eval echo "{$number1..$number2}")
do
        rem=$(($i % 2))
        if [ "$rem" -eq "0" ]; then
                echo $i
        fi
done
