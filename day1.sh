#/bin/sh
sed -rn 's/[a-zA-Z]//g ; s/^([0-9])([0-9])*([0-9])?/\1\2/ ; s/^([0-9])$/\1\1/ ; G ; P' - | tr '\n' '+' | xargs -I% echo % "0" | bc
