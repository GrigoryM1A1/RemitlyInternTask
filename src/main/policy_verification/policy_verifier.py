from policy_verification.policy_reader_service import PolicyReaderService
import re


class PolicyVerifier:
    name_key: str = "PolicyName"
    document_key: str = "PolicyDocument"
    statement_key: str = "Statement"
    version_key: str = "Version"
    resource_key: str = "Resource"
    policy_name_pattern: str = r"[\w+=,.@-]+"

    def __init__(self, absolute_path: str) -> None:
        self.path: str = absolute_path
        self.policy_reader: PolicyReaderService = PolicyReaderService()
        self.policy: dict = self.policy_reader.read_policy_from_json(self.path)

    def verify(self) -> bool:
        if not self.policy:
            raise OSError("[ERROR] Failed to load the given file")
        
        if self.policy.keys() != {self.name_key, self.document_key}:
            raise KeyError(f"[ERROR] Policy must have these keys: {self.name_key} and {self.document_key}")

        if self.verify_policy_name() and self.verify_policy_document():
            return True
        
        return False
    
    def verify_policy_name(self) -> bool:
        name = self.policy[self.name_key]

        if not isinstance(name, str):
            raise ValueError("PolicyName must be string")
        
        if not re.fullmatch(self.policy_name_pattern, name):
            raise ValueError("PolicyName must have this pattern: [\w+=,.@-]+")
        
        if not 1 <= len(name) <= 128:
            raise ValueError("PolicyName length must be between 1-128")
        
        return True
        

    def verify_policy_document(self):
        if not isinstance(self.policy[self.document_key], dict):
            raise TypeError(f"[ERROR] Type of {self.document_key} must be dict")
        
        document: dict = self.policy[self.document_key]
        if not self.version_key in document:
            raise KeyError(f"[ERROR] PolicyDocument must have this key: {self.version_key}")
        
        if not self.statement_key in document:
            raise KeyError(f"[ERROR] PolicyDocument must have this key: {self.statement_key}")
        
        if isinstance(document[self.statement_key], list):
            return self.verify_multiple_statements(document[self.statement_key])
        
        elif isinstance(document[self.statement_key], dict):
            return self.verify_single_statement(document[self.statement_key])
        
        else: raise TypeError(f"[ERROR] Statement must be one of these types: dict or list")
    
    def verify_single_statement(self, statement: dict) -> bool:
        if self.resource_key in statement and statement[self.resource_key] == "*":
            return False
        return True

    def verify_multiple_statements(self, statements: list) -> bool:
        for statement in statements:
            if not isinstance(statement, dict):
                raise TypeError(f"[ERROR] If statement is given by list then all of its content must be of type dict")
        
        for statement in statements:
            if not self.verify_single_statement(statement):
                return False
        return True       

        