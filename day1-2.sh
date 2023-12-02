#/bin/sh
sed -rn ':x ; s/(one|two|three|four|five|six|seven|eight|nine)(.*)/\1 \2/; { s/one /1/; s/two /2/; s/three /3/; s/four /4/; s/five /5/; s/six /6/; s/seven /7/; s/eight /8/ ; s/nine /9/ } ; tx ; s/[a-z ]//g ; P ' - | sed -rn 's/[a-zA-Z]//g ; s/^([0-9])([0-9])*([0-9])?/\1\2/ ; s/^([0-9])$/\1\1/ ; G ; P' | tr '\n' '+' | xargs -I% echo % "0" | bc
