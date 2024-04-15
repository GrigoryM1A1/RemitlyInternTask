import json


class PolicyReaderService:
    def read_policy_from_json(self, path: str) -> dict:
        policy: dict = {}
        try:
            with open(path) as json_file:
                policy = json.load(json_file)
        except FileNotFoundError:
            print("[ERROR] Given file not found")
            return {}
        except PermissionError:
            print(f"[ERROR] You have no permission to this file {path}")
            return {}
        except json.decoder.JSONDecodeError:
            print("[ERROR] Failed to decode the file")
            return {}
        except OSError:
            print(f"[ERROR] Could not open file with given path {path}")
            return {}
        except Exception as e:
            print(f"[ERROR] Unpredicted error occured: {e}")
            return {}
        
        return policy