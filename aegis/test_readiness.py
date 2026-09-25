from readiness import ReadinessState, introduction_gate

def test_readiness_precedes_introduction():
    allowed,missing=introduction_gate(ReadinessState(True,True,True,True))
    assert allowed and not missing

def test_matching_does_not_bypass_authenticity():
    allowed,missing=introduction_gate(ReadinessState(True,True,False,True))
    assert not allowed and "AUTHENTICITY" in missing
