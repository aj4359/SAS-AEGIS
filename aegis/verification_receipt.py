from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class HumanVerificationReceipt:
    subject_id: str
    provider_ref: str
    verified: bool
    verified_at: datetime
    method_class: str

FORBIDDEN_RELATIONSHIP_FIELDS = {
    "compatibility_score","messages","preferences","relationship_answers","biometric_payload"
}

def assert_minimal_verification_record(record: dict) -> None:
    forbidden = FORBIDDEN_RELATIONSHIP_FIELDS.intersection(record.keys())
    if forbidden:
        raise ValueError(f"Identity verification record contains forbidden relationship/biometric fields: {sorted(forbidden)}")
