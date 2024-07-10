import pytest
import os
from app.utils.fileloader import FileLoader


@pytest.fixture
def setup_files(tmp_path):
    os.chdir(tmp_path)
    (tmp_path / "file1").touch()
    (tmp_path / "file2").touch()
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    (dir1 / "file3").touch()
    (dir1 / "file4").touch()

    return tmp_path


@pytest.fixture
def setup_env_files(tmp_path):
    os.chdir(tmp_path)
    env_path = tmp_path / ".env"
    env_path.write_text("TEST_VAR=test_value")
    env_local_path = tmp_path / ".env.local"
    env_local_path.write_text("LOCAL_VAR=local_value")

    return env_path, env_local_path


class TestFileLoader:
    @staticmethod
    def test_init(tmp_path):
        os.chdir(tmp_path)
        app_path = tmp_path / "app"
        public_path = app_path / "public"
        app_path.mkdir()
        public_path.mkdir()

        file_loader = FileLoader()

        checks = [
            file_loader.DIRPATHS.ROOT == str(tmp_path),
            file_loader.DIRPATHS.APP == str(app_path),
            file_loader.DIRPATHS.PUBLIC == str(public_path),
            file_loader.FILEPATHS.ENV_PROD == ".env",
            file_loader.FILEPATHS.ENV_LOCAL == ".env.local",
        ]
        assert all(checks)

    @staticmethod
    def test_finder_for_files(setup_files):
        tmp_path = setup_files

        def condition_func(target, files, dirs):
            return target in files

        targets = ["file1", "file3"]
        result = FileLoader.finder(targets, condition_func)
        assert result == [str(tmp_path / "file1"), str(tmp_path / "dir1" / "file3")]

    @staticmethod
    def test_is_file(setup_files):
        tmp_path = setup_files
        files = os.listdir(tmp_path)
        dirs = [d for d in os.listdir(tmp_path) if os.path.isdir(tmp_path / d)]

        checks = [
            FileLoader.is_file("file1", files, dirs) is True,
            FileLoader.is_file("file3", files, dirs) is False,
        ]
        assert all(checks)

    @staticmethod
    def test_is_dir(setup_files):
        tmp_path = setup_files
        files = [f for f in os.listdir(tmp_path) if os.path.isfile(tmp_path / f)]
        dirs = [d for d in os.listdir(tmp_path) if os.path.isdir(tmp_path / d)]

        checks = [
            FileLoader.is_dir("dir1", files, dirs) is True,
            FileLoader.is_dir("dir3", files, dirs) is False,
        ]
        assert all(checks)

    @staticmethod
    def test_prod_dotenv(setup_env_files, monkeypatch):
        env_path, _ = setup_env_files
        monkeypatch.setenv("DOTENV_PATH", str(env_path))
        file_loader = FileLoader()
        file_loader.prod_dotenv()
        assert os.getenv("TEST_VAR") == "test_value"

    @staticmethod
    def test_local_dotenv(setup_env_files, monkeypatch):
        _, env_local_path = setup_env_files
        monkeypatch.setenv("DOTENV_LOCAL_PATH", str(env_local_path))
        file_loader = FileLoader()
        file_loader.local_dotenv()
        assert os.getenv("LOCAL_VAR") == "local_value"
