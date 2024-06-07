docker compose -f docker-compose-test.yaml run --rm myapp

# $? will contain the exit code of the docker run command
# (which reflects the pytest command's exit code)
exit_code=$?
# print exit code
echo "Exit code: $exit_code"

if [ $exit_code -eq 0 ]; then
  echo "Pytest tests passed!"
else
  echo "Pytest tests failed! (exit code: $exit_code)"
fi