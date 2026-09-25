import pytest
from human_authenticity import (
    IdentityType, ProspectIdentity, VerificationState,
    assert_assistant_disclosed, assert_no_romantic_impersonation,
    may_display_human_verified, may_enter_human_prospect_pool,
)

def test_verified_human_is_allowed_and_badged():
    p = ProspectIdentity("h1", IdentityType.HUMAN, VerificationState.VERIFIED)
    assert may_enter_human_prospect_pool(p)
    assert may_display_human_verified(p)

def test_unresolved_identity_is_not_human_verified():
    p = ProspectIdentity("u1", IdentityType.UNRESOLVED, VerificationState.UNVERIFIED)
    assert not may_enter_human_prospect_pool(p)
    assert not may_display_human_verified(p)

def test_synthetic_persona_blocked_from_human_pool_and_impersonation():
    p = ProspectIdentity("s1", IdentityType.SYNTHETIC, VerificationState.VERIFIED)
    assert not may_enter_human_prospect_pool(p)
    with pytest.raises(PermissionError):
        assert_no_romantic_impersonation(p, acting_as_prospect=True)

def test_disclosed_assistant_is_permitted():
    a = ProspectIdentity("a1", IdentityType.SERVICE_ASSISTANT, VerificationState.VERIFIED, True)
    assert_assistant_disclosed(a)

def test_undisclosed_assistant_is_blocked():
    a = ProspectIdentity("a2", IdentityType.SERVICE_ASSISTANT, VerificationState.VERIFIED, False)
    with pytest.raises(PermissionError):
        assert_assistant_disclosed(a)
