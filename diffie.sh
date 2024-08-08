. ./conversion.sh

# echo "Welcome to the Diffie-Hellman key exchange protocol for sending big files securely. \n"

# echo "Please enter the prime number: "
# primary_key=23

# echo "\n Please enter the primitive root: "
# primitive_root=5

# echo "\n Please enter the Public key for yourself: "
# public_key=15

# # Call the function with "Joseph"
# echo "Please enter the word: \n"
# read private_word
# private_key=$(con_private_word $private_word)
# echo "The ASCII sum of the word $private_word is: $private_key"

private_key=116

r=$(cal_secret $primary_key $primitive_root $private_key $public_key)
echo "The secret is $r"


