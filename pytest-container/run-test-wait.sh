container_id=$(docker run --rm pytest)

# echo container id
eho "Container ID: $container_id"

exit_code=$(docker wait $container_id)

if [ $exit_code -eq 0 ]; then
  echo "Pytest tests passed!"
else
  echo "Pytest tests failed! (exit code: $exit_code)"
fi
