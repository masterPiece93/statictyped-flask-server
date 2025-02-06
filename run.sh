echo "Greetings , Attempting to run the Flask Server ...."

echo "executing static typechecker"

mypy server.py --follow-imports normal --strict

# python3 server.py