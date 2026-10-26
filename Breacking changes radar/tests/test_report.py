# tests/test_report.py

from breaking_changes_radar.models.report import Report, Severity
import pytest

def test_report_creation():
    report = Report(severity=Severity.CRITICAL, impact_score=10, affected_symbols=['func1'])
    assert report.severity == Severity.CRITICAL
    assert report.impact_score == 10
    assert report.affected_symbols == ['func1']