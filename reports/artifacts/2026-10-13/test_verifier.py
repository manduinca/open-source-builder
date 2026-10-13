"""Pruebas offline del verificador; nunca consultan ni modifican GitHub."""
import unittest
from unittest.mock import patch

import verify_candidates as verifier


class CandidateVerificationTests(unittest.TestCase):
    def issue(self, body="", state="open", assignees=None):
        return {
            "html_url": "https://github.com/example/project/issues/1",
            "title": "Example", "state": state, "user": {"login": "reporter"},
            "created_at": "2026-10-13T00:00:00Z",
            "updated_at": "2026-10-13T00:00:00Z",
            "assignees": assignees or [], "labels": [], "body": body,
        }

    def verify(self, issue, comments=(), references=(), closers=(), complete=True):
        with patch.object(verifier, "gh", return_value=issue), patch.object(
            verifier, "pages", side_effect=[
                (list(comments), complete), (list(references), complete),
                (list(closers), complete),
            ],
        ):
            return verifier.verify(issue["html_url"])

    def test_body_offer_is_signal_not_assignment(self):
        result = self.verify(self.issue(
            "Would you like to help contributing this feature?\n\nYes"))
        self.assertTrue(result["bodyOfferSignal"])
        self.assertTrue(result["passesMechanicalChecks"])

    def test_connected_and_closing_prs_deduplicate_and_block(self):
        pr = {"url": "https://github.com/example/project/pull/2", "state": "OPEN"}
        result = self.verify(self.issue(), references=[
            {"source": None, "subject": pr}, {"source": pr},
        ], closers=[pr])
        self.assertEqual(result["referencesCount"], 1)
        self.assertEqual(result["openLinkedPrs"], [pr])
        self.assertFalse(result["passesMechanicalChecks"])

    def test_incomplete_history_does_not_pass(self):
        result = self.verify(self.issue(), complete=False)
        self.assertFalse(result["historyComplete"])
        self.assertFalse(result["passesMechanicalChecks"])

    def test_closed_issue_or_assigned_issue_does_not_pass(self):
        self.assertFalse(self.verify(self.issue(state="closed"))[
            "passesMechanicalChecks"])
        self.assertFalse(self.verify(self.issue(assignees=[{"login": "worker"}]))[
            "passesMechanicalChecks"])

    def test_offer_in_comment_is_signal(self):
        result = self.verify(self.issue(), comments=[{
            "body": "I'm happy to implement this", "url": "example", }])
        self.assertEqual(len(result["claimSignals"]), 1)

    def test_rejects_non_issue_or_non_github_url(self):
        for url in ("https://example.com/o/r/issues/1",
                    "https://github.com/o/r/pull/1"):
            with self.assertRaises(ValueError):
                verifier.verify(url)


if __name__ == "__main__":
    unittest.main()
