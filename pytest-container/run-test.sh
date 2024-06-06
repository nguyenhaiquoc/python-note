IMAGE_NAME='pytest-container:latest'
docker run --rm $IMAGE_NAME pytest

# $? will contain the exit code of the docker run command
# (which reflects the pytest command's exit code)
exit_code=$?

if [ $exit_code -eq 0 ]; then
  echo "Pytest tests passed!"
else
  echo "Pytest tests failed! (exit code: $exit_code)"
fi