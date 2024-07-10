import pytest
import os
from app.config.env import finder, load_dotenv_file


@pytest.fixture
def env_file(tmp_path):
    """Fixture to create a mock dotenv file."""
    os.chdir(tmp_path)
    env_file = tmp_path / ".env.local"
    env_file.write_text("TEST_VAR=value")
    return env_file


class TestFinder:
    @staticmethod
    def test_file_exists(env_file):
        result = finder(".env.local")
        assert result == str(env_file)


class TestLoadDotenvFile:
    @staticmethod
    def test_success(env_file, monkeypatch):
        monkeypatch.setenv("DOTENV_LOCAL_PATH", str(env_file))
        load_dotenv_file(env_file)
        assert os.getenv("TEST_VAR") == "value"
