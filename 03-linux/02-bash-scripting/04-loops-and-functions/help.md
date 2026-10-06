# Help — Loops, functions and numeric validation

## First hint

Check digits and length before numeric conversion.

## Detailed approach

Use [[ "$value" =~ ^[0-9]+$ ]], ${#value} for length and $((10#$value)) for a validated nonempty token. Check length before conversion. At most 100 * 1000000 fits the supported 64-bit lab. Initialize total=0 and use total=$((total + number)). Print once after validation/accumulation; no partial output on error.

## Troubleshooting

08 without a decimal prefix can fail as octal. Arithmetic expressions such as 1+2 are not valid input values.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
