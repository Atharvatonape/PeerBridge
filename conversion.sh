take_only_int() {
    while true; do
        read -p "Please enter an integer: " root
        if [[ "$root" =~ ^-?[0-9]+$ ]]; then
            echo "You entered a valid integer: $root"
            break
        else
            echo "Invalid input. Please enter a valid integer."
        fi
    done
    return $root
}

con_private_word() {
    local word=$1
    local sum
    for (( i=0; i<${#word}; i++ )); do
        char="${word:$i:1}"
        ascii=$(printf "%d" "'$char")
        sum+=$ascii
    done
    echo $sum
}


