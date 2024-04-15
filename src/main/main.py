from policy_verification.policy_verifier import PolicyVerifier


if __name__ == "__main__":
    absolute_path: str = input("Absolute path to the policy: ")
    try:
        verifier = PolicyVerifier(absolute_path)
        print(verifier.verify())
    except (OSError, KeyError, ValueError, TypeError) as e:
        print(e)