"""Provided behavior tests for the stable fixture app."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
import app

COURSE = Path(__file__).resolve().parents[1]


class AppTests(unittest.TestCase):
    def setUp(self):
        self.lab = tempfile.TemporaryDirectory(prefix="le_app_test_")
        self.addCleanup(self.lab.cleanup)
        self.root = Path(self.lab.name)
        self.output = self.root / "output"

    def write_input(self, text):
        path = self.root / "input.csv"
        path.write_text(text, encoding="utf-8")
        return path

    def test_fixture_and_replay(self):
        expected = {"input_rows": 6, "accepted_rows": 4, "rejected_rows": 2, "event_count": 3, "total_cents": 3050}
        source = COURSE / "data" / "events.csv"
        original = source.read_bytes()
        self.assertEqual(app.run(source, self.output), expected)
        self.assertEqual(app.run(source, self.output), expected)
        self.assertEqual(json.loads((self.output/"report.json").read_text()), {"event_count": 3, "total_cents": 3050})
        bad = [json.loads(line) for line in (self.output/"rejected.jsonl").read_text().splitlines()]
        self.assertEqual([(r["record_number"],r["reason"]) for r in bad], [(6,"amount"),(7,"id")])
        self.assertEqual(source.read_bytes(), original)

    def test_empty(self):
        result = app.run(self.write_input("event_id,amount_cents\n"), self.output)
        self.assertEqual(result, {"input_rows":0,"accepted_rows":0,"rejected_rows":0,"event_count":0,"total_cents":0})

    def test_conflict_preserves_prior_output(self):
        app.run(COURSE/"data"/"events.csv", self.output)
        before = {p.name:p.read_bytes() for p in self.output.iterdir()}
        source = self.write_input("event_id,amount_cents\nA,1\nA,2\n")
        with self.assertRaises(ValueError):
            app.run(source, self.output)
        self.assertEqual({p.name:p.read_bytes() for p in self.output.iterdir()}, before)

    def test_header_and_shape(self):
        for body in ["event_id,event_id\nA,1\n", "event_id,amount_cents\nA\n", "event_id,amount_cents\nA,1,extra\n"]:
            with self.subTest(body=body), self.assertRaises(ValueError):
                app.run(self.write_input(body), self.output)

    def test_cli_failure_status_and_stderr(self):
        output, errors = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            result = app.main(["--input",str(self.root/"missing.csv"),"--output",str(self.output)])
        self.assertEqual(result,2)
        self.assertEqual(output.getvalue(),"")
        self.assertEqual(json.loads(errors.getvalue())["event"],"run_failed")
        self.assertFalse(self.output.exists())

    def test_output_directory_collision(self):
        target = self.root/"occupied"
        target.write_text("preserve",encoding="utf-8")
        with self.assertRaises(OSError):
            app.run(COURSE/"data"/"events.csv",target)
        self.assertEqual(target.read_text(),"preserve")


if __name__ == "__main__":
    unittest.main()
