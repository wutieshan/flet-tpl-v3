import json
import os
import tomllib


class FileUtil:
    @classmethod
    def get_abs_path(cls, filepath: str) -> str:
        """get absolute path from relative path."""
        return os.path.join(os.path.abspath("."), filepath)

    @classmethod
    def ensure_path_exists(cls, path: str, is_filepath: bool = True) -> None:
        """ensure the directory path exists, create if not."""
        abspath = cls.get_abs_path(path)
        if is_filepath:
            abspath = os.path.dirname(abspath)

        if not os.path.exists(abspath):
            os.makedirs(abspath)

    @classmethod
    def parse_dict(cls, filepath: str) -> dict:
        """parse file content into a dictionary.
        
        args:
            filepath: path to the file to parse
            
        returns:
            dict: parsed data
            
        raises:
            FileNotFoundError: if file doesn't exist
            PermissionError: if no read permission
            ValueError: if file format is invalid
            NotImplementedError: if file type is not supported
        """
        filepath = cls.get_abs_path(filepath)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"file not found: {filepath}")
            
        if not os.access(filepath, os.R_OK):
            raise PermissionError(f"no read permission for file: {filepath}")
            
        with open(filepath, "rb") as fp:
            ext = os.path.splitext(filepath)[1].lower()
            match ext:
                case ".json":
                    data = json.load(fp)
                case ".toml":
                    data = tomllib.load(fp)
                case _:
                    raise NotImplementedError(f"unsupported file type: {ext}")
            return data
