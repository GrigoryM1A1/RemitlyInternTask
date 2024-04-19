from policy_verification.policy_verifier import PolicyVerifier
from policy_verification.policy_reader_service import PolicyReaderService
from json.decoder import JSONDecodeError


if __name__ == "__main__":
    absolute_path: str = input("Absolute path to the policy: ")
    try:
        verifier = PolicyVerifier(absolute_path, PolicyReaderService())
        print(verifier.verify())
    except (
            KeyError,
            ValueError,
            TypeError,
            FileNotFoundError,
            PermissionError,
            OSError,
            JSONDecodeError,
            Exception
        ) as e:
        print(e)