from dataclasses import dataclass

@dataclass(frozen=True)
class ReadinessState:
    self_understanding_complete: bool
    intentions_declared: bool
    authenticity_resolved: bool
    consent_to_introduction: bool

def introduction_gate(state: ReadinessState) -> tuple[bool, tuple[str, ...]]:
    missing=[]
    if not state.self_understanding_complete: missing.append("SELF_UNDERSTANDING")
    if not state.intentions_declared: missing.append("INTENTIONS")
    if not state.authenticity_resolved: missing.append("AUTHENTICITY")
    if not state.consent_to_introduction: missing.append("CONSENT")
    return (not missing, tuple(missing))
