#!/bin/bash

if [[ $1 != "{xor}"* ]]; then
    data="$1"
else
    data="${1:5}"
fi

# Base64-dən hex-ə çeviririk, sonra hər hex cütünü 5f (_) ilə XOR edirik
decoded=$(echo -n "$data" | base64 -d | xxd -p -c1 | while read hex; do
    printf "\\x$(printf '%x' $((0x$hex ^ 0x5f)))"
done)

echo -e "$decoded"
