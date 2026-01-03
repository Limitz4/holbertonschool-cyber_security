#!/bin/bash
if [ "$#" -ne 1 ]; then
    exit 1
fi
DOMAIN=$1
whois "$DOMAIN" | awk -F': ' '
BEGIN {
    fields = "Name,Organization,Street,City,State/Province,Postal Code,Country,Phone,Phone Ext,Fax,Fax Ext,Email"
    split(fields, subf, ",")
    cats[1] = "Registrant"; cats[2] = "Admin"; cats[3] = "Tech"
}
{
    gsub(/\r/, "")
    for (i=1; i<=3; i++) {
        for (j=1; j<=12; j++) {
            pattern = "^" cats[i] " " subf[j] ":"
            if ($0 ~ pattern) {
                val = $0
                sub(/^[^:]+:[ \t]*/, "", val)
                data[i,j] = val
            }
        }
    }
}
END {
    out = ""
    for (i=1; i<=3; i++) {
        for (j=1; j<=12; j++) {
            f_name = cats[i] " " subf[j]
            val = data[i,j]
            if (subf[j] == "Street" && val != "") val = val " "
            if (subf[j] ~ /Ext/) f_name = f_name ":"
            out = out f_name "," val "\n"
        }
    }
    printf "%s", substr(out, 1, length(out)-1)
}
' > "$DOMAIN.csv"
