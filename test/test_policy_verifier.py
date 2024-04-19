import unittest
from unittest.mock import MagicMock
import test.test_resources.test_cases as res
from src.main.policy_verification.policy_reader_service import PolicyReaderService
from src.main.policy_verification.policy_verifier import PolicyVerifier


class PolicyVerifierTest(unittest.TestCase):
    def test_verify(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.policy1)
        verifier = PolicyVerifier("/path/policy1.json", reader)
        self.assertFalse(verifier.verify())

        reader.read_policy_from_json = MagicMock(return_value=res.policy2)
        verifier = PolicyVerifier("/path/policy2.json", reader)
        self.assertFalse(verifier.verify())

        reader.read_policy_from_json = MagicMock(return_value=res.policy3)
        verifier = PolicyVerifier("/path/policy3.json", reader)
        self.assertTrue(verifier.verify())

        reader.read_policy_from_json = MagicMock(return_value=res.policy4)
        verifier = PolicyVerifier("/path/policy4.json", reader)
        self.assertTrue(verifier.verify())

    def test_key_error(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.key_error1)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(KeyError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.key_msg)

        reader.read_policy_from_json = MagicMock(return_value=res.key_error2)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(KeyError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.key_msg)

        reader.read_policy_from_json = MagicMock(return_value=res.key_error3)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(KeyError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.key_msg)

    def test_policy_name_type(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.name_type_error)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(TypeError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.name_type_msg)

    def test_policy_name_regex(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.name_length_error)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(ValueError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.name_length_msg)

    def test_policy_name_length(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.name_regex_error1)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(ValueError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.name_regex_msg)

        reader.read_policy_from_json = MagicMock(return_value=res.name_regex_error2)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(ValueError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.name_regex_msg)

    def test_document_type(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.document_type_error1)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(TypeError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.document_type_msg)

        reader.read_policy_from_json = MagicMock(return_value=res.document_type_error1)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(TypeError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.document_type_msg)

    def test_version_key(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.version_key_error)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(KeyError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.version_key_msg)

    def test_statement_key(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.statement_key_error)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(KeyError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.statement_key_msg)

    def test_statement_type(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.statement_type_error1)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(TypeError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.statement_type_msg)

        reader.read_policy_from_json = MagicMock(return_value=res.statement_type_error2)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(TypeError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.statement_type_msg)

    def test_statement_elements_type(self):
        reader = PolicyReaderService()
        reader.read_policy_from_json = MagicMock(return_value=res.statement_element_type_error1)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(TypeError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.statement_element_type_msg)

        reader.read_policy_from_json = MagicMock(return_value=res.statement_element_type_error2)
        verifier = PolicyVerifier("/path/policy.json", reader)
        with self.assertRaises(TypeError) as error:
            verifier.verify()
        self.assertEqual(error.exception.args[0], res.statement_element_type_msg)

if __name__ == "__main__":
    unittest.main()