import json


class PolicyReaderService:
    def read_policy_from_json(self, path: str) -> dict:
        policy: dict = {}
        try:
            with open(path) as json_file:
                policy = json.load(json_file)
        except FileNotFoundError:
            raise FileNotFoundError("[ERROR] Given file not found")
        except PermissionError:
            raise PermissionError(f"[ERROR] You have no permission to this file {path}")
        except json.decoder.JSONDecodeError as e:
            raise json.decoder.JSONDecodeError("[ERROR] Failed to decode the file", e.doc, e.pos)
        except OSError:
            raise OSError(f"[ERROR] Could not open file with given path {path}")
        except Exception as e:
            raise Exception(f"[ERROR] Unpredicted error occured: {e}")
        
        return policy