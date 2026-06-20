#!/bin/bash

# Configuration: Eligible criteria
VALID_COUNTRIES=("Uganda" "Kenya" "Tanzania")
MIN_AGE=18
MAX_AGE=35

echo "--- Workshop Registration ---"

# Collect inputs
read -p "Enter your Surname: " surname
read -p "Enter your Name: " name
read -p "Enter your Age: " age
read -p "Enter your Country: " country

# Validate Age (must be a number)
if ! [[ "$age" =~ ^[0-9]+$ ]]; then
    echo "Error: Age must be a number."
    exit 1
fi

# Check Age eligibility
if (( age < MIN_AGE || age > MAX_AGE )); then
    echo "Sorry $name $surname, you are not eligible. Age must be between $MIN_AGE and $MAX_AGE."
    exit 1
fi

# Check Country eligibility
is_country_valid=false
for c in "${VALID_COUNTRIES[@]}"; do
    if [[ "$country" == "$c" ]]; then
        is_country_valid=true
        break
    fi
done

if [ "$is_country_valid" = false ]; then
    echo "Sorry $name $surname, the workshop is only for: ${VALID_COUNTRIES[*]}."
    exit 1
fi

# Success message
echo "------------------------------------------------"
echo "Success! Welcome to the workshop, $name $surname."
echo "Your registration has been confirmed."
echo "------------------------------------------"
