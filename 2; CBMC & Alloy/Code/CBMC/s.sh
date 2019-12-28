# cbmc add_numbers.c --unwind 3 --bounds-check --pointer-check --trace --unwinding-assertions --function add_numbers
# cbmc comp_rem.c --unwind 3 --bounds-check --pointer-check --trace --unwinding-assertions --function compute_remainder
# cbmc comp_quot.c --unwind 3 --bounds-check --pointer-check --trace --unwinding-assertions --function compute_quotient
# cbmc gcd_for.c --unwind 100 --bounds-check --pointer-check --trace --function gcd
# cbmc gcd_while.c --unwind 100 --bounds-check --pointer-check --trace --function gcd
# cbmc swap.c --unwind 6 --bounds-check --pointer-check --trace --function swap
# cbmc array_access.c --unwind 10 --bounds-check --pointer-check --unwinding-assertions --trace --function access
# cbmc reverse.c --unwind 10 --bounds-check --pointer-check --trace --function reverse