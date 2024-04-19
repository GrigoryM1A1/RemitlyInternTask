import unittest
import test.test_resources.test_cases as res
from unittest.mock import patch, mock_open
from src.main.policy_verification.policy_reader_service import PolicyReaderService
import json


class PolicyReaderServiceTest(unittest.TestCase):
    def test_read_valid_json(self):
        with patch("builtins.open", mock_open(read_data=json.dumps(res.json1))):
            reader = PolicyReaderService()
            self.assertEqual(reader.read_policy_from_json("/resources/policy.json"), {"PolicyName": "TestPolicy"})

        with patch("builtins.open", mock_open(read_data=json.dumps(res.json2))):
            reader = PolicyReaderService()
            self.assertEqual(reader.read_policy_from_json("/resources/policy.json"), {"PolicyName": "name", "PolicyDocument": "document"})   
    
    def test_read_nonexistent_json(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            reader = PolicyReaderService()
            with self.assertRaises(FileNotFoundError) as error:
                reader.read_policy_from_json("/resource/nopolicy.json")
            self.assertEqual(error.exception.args[0], res.file_not_found_msg)
        
    def test_read_no_permission_error(self):
        with patch("builtins.open", side_effect=PermissionError):
            reader = PolicyReaderService()
            with self.assertRaises(PermissionError) as error:
                reader.read_policy_from_json("/resources/nopermission.json")
            self.assertEqual(error.exception.args[0], res.permission_error_msg)

    def test_read_policy_JSONDecodeError(self):
        with patch("builtins.open", mock_open(read_data='{"PolicyName": "name"}}')):
            reader = PolicyReaderService()
            with self.assertRaises(json.decoder.JSONDecodeError) as context:
                reader.read_policy_from_json("/bad/json_format.json")

            self.assertEqual(str(context.exception), res.json_decoder_msg)
            self.assertEqual(context.exception.doc, '{"PolicyName": "name"}}')
            self.assertEqual(context.exception.pos, 22)


    def test_OSError_raise(self):
        with patch("builtins.open", side_effect=OSError):
            reader = PolicyReaderService()
            with self.assertRaises(OSError) as error:
                reader.read_policy_from_json("/wrong/path")
            self.assertEqual(error.exception.args[0], res.os_error_msg)

    def test_other_exception(self):
        with patch("builtins.open", side_effect=Exception):
            reader = PolicyReaderService()
            with self.assertRaises(Exception) as error:
                reader.read_policy_from_json("/unpredictable")
            self.assertEqual(error.exception.args[0], res.exception_msg)

if __name__ == "__main__":
    unittest.main()