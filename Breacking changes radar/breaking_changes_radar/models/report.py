# breaking_changes_radar.models.report
# breaking_changes_radar/models/report.py

from pydantic import BaseModel, Field
from typing import List  # Ensure this line is present

class Severity(str):
    CRITICAL = 'CRITICAL'
    MAJOR = 'MAJOR'
    MINOR = 'MINOR'

class Report(BaseModel):
    severity: Severity = Field(..., description='The severity of the breaking change.')
    impact_score: int = Field(..., description='The impact score of the breaking change.')
    affected_symbols: List[str] = Field(..., description='The symbols affected by the breaking change.')

