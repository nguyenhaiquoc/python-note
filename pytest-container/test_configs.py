from configs import Config  # Import the Config class from the config module


def test_config_reads_env_file():
    # Create an instance of the Config class
    config = Config()

    # Assert that the config object has the expected values from the .env file
    assert config.DB_HOST == "prod-host"
