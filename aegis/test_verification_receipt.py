import unittest
from verification_receipt import assert_minimal_verification_record

class VerificationReceiptTests(unittest.TestCase):
    def test_minimal_identity_receipt_allowed(self):
        assert_minimal_verification_record({"subject_id":"h1","provider_ref":"p1","verified":True,"method_class":"document"})

    def test_relationship_data_cannot_leak_into_identity_record(self):
        with self.assertRaises(ValueError):
            assert_minimal_verification_record({"subject_id":"h1","verified":True,"relationship_answers":["x"]})

    def test_raw_biometric_payload_is_forbidden(self):
        with self.assertRaises(ValueError):
            assert_minimal_verification_record({"subject_id":"h1","biometric_payload":"raw"})

if __name__=="__main__":
    unittest.main()
