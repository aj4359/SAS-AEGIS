from dataclasses import dataclass
from enum import Enum

class IdentityType(str, Enum):
    HUMAN = "human"
    SYNTHETIC = "synthetic"
    SERVICE_ASSISTANT = "service_assistant"
    UNRESOLVED = "unresolved"

class VerificationState(str, Enum):
    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    FAILED = "failed"

@dataclass(frozen=True)
class ProspectIdentity:
    identity_id: str
    identity_type: IdentityType
    verification: VerificationState
    machine_assistance_disclosed: bool = False

def may_enter_human_prospect_pool(identity: ProspectIdentity) -> bool:
    return identity.identity_type is IdentityType.HUMAN

def may_display_human_verified(identity: ProspectIdentity) -> bool:
    return (
        identity.identity_type is IdentityType.HUMAN
        and identity.verification is VerificationState.VERIFIED
    )

def assert_no_romantic_impersonation(identity: ProspectIdentity, acting_as_prospect: bool) -> None:
    if acting_as_prospect and identity.identity_type is not IdentityType.HUMAN:
        raise PermissionError("Human Authenticity block: non-human identity cannot impersonate a romantic prospect")

def assert_assistant_disclosed(identity: ProspectIdentity) -> None:
    if identity.identity_type is IdentityType.SERVICE_ASSISTANT and not identity.machine_assistance_disclosed:
        raise PermissionError("Human Authenticity block: machine assistance must be disclosed")
