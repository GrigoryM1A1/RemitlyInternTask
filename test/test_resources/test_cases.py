# error messages
file_not_found_msg = "[ERROR] Given file not found"
permission_error_msg = "[ERROR] You have no permission to this file /resources/nopermission.json"
os_error_msg = "[ERROR] Could not open file with given path /wrong/path"
exception_msg = "[ERROR] Unpredicted error occured: "
json_decoder_msg = "[ERROR] Failed to decode the file: line 1 column 23 (char 22)"


key_msg = "[ERROR] Policy must have these keys: PolicyName and PolicyDocument"
name_type_msg = "PolicyName must be string"
name_length_msg = "PolicyName length must be between 1-128"
name_regex_msg = "PolicyName must have this pattern: [\w+=,.@-]+"
document_type_msg = "[ERROR] Type of PolicyDocument must be dict"
version_key_msg = "[ERROR] PolicyDocument must have this key: Version"
statement_key_msg = "[ERROR] PolicyDocument must have this key: Statement"
statement_type_msg = "[ERROR] Statement must be one of these types: dict or list"
statement_element_type_msg = "[ERROR] If statement is given by list then all of its content must be of type dict"

# mocked jsons to read
json1 = {"PolicyName": "TestPolicy"}
json2 = {"PolicyName": "name", "PolicyDocument": "document"}

# mocked policies to verify with valid format
# false
policy1 = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}

# false
policy2 = {
    "PolicyName": "root",
    "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "FirstStatement",
        "Effect": "Allow",
        "Action": ["iam:ChangePassword"],
        "Resource": "*"
      },
      {
        "Sid": "SecondStatement",
        "Effect": "Allow",
        "Action": "s3:ListAllMyBuckets",
        "Resource": "*"
      },
      {
        "Sid": "ThirdStatement",
        "Effect": "Allow",
        "Action": [
          "s3:List*",
          "s3:Get*"
        ],
        "Resource": [
          "arn:aws:s3:::confidential-data",
          "arn:aws:s3:::confidential-data/*"
        ],
        "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
      }
    ]
  }
}

# true
policy3 = {
    "PolicyName": "root",
    "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example_bucket"
    }
}
}

# true
policy4 = {
    "PolicyName": "root",
    "PolicyDocument": {
      "Version": "2012-10-17",
      "Statement": [{
        "Sid": "1",
        "Effect": "Allow",
        "Principal": {"AWS": ["arn:aws:iam::account-id:root"]},
        "Action": "s3:*",
        "Resource": [
          "arn:aws:s3:::mybucket",
          "arn:aws:s3:::mybucket/*"
        ]
      }]
}}


# raising with errors
key_error1 = {"PolicyName": "root"}

key_error2 = {"PolicyName": "root", "WrongKey": "key"}

key_error3 = {"PolicyName": "root", "PolicyDocument": {}, "OtherKey": 1}

name_length_error = {
    "PolicyName": "@" * 130, "PolicyDocument": {}
}

name_regex_error1 = {
    "PolicyName": "", "PolicyDocument": {}
}

name_regex_error2 = {
    "PolicyName": "`", "PolicyDocument": {}
}

name_type_error = {
    "PolicyName": 1, "PolicyDocument": {}
}

document_type_error1 = {
    "PolicyName": "name", "PolicyDocument": [1, 2, 3]
}

document_type_error2 = {
    "PolicyName": "name", "PolicyDocument": "document"
}

version_key_error = {
    "PolicyName": "name", "PolicyDocument": {"Statement": "*", "NotVersion": "x"}
}

statement_key_error = {
    "PolicyName": "name", "PolicyDocument": {"Version": "*", "NotVersion": "x"}
}

statement_type_error1 = {
    "PolicyName": "name", "PolicyDocument": {"Version": "*", "Statement": 3}
}

statement_type_error2 = {
    "PolicyName": "name", "PolicyDocument": {"Version": "*", "Statement": "x"}
}

statement_element_type_error1 = {
    "PolicyName": "name", "PolicyDocument": {
        "Version": "*",
        "Statement": [
            21, {}, ""
        ]
    }
}

statement_element_type_error2 = {
    "PolicyName": "name",
    "PolicyDocument": {
        "Version": "*",
        "Statement": [
            {}, {}, "", 1, {}
        ]
    }
}
