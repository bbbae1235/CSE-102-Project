#!/bin/bash

# Loop from 1 to 4
for i in {1..4}
do
    # Run the command with the current value of i
    ./MWST "in$i" "out$i"
done

