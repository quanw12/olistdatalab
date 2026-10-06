"""Provided behavioral checks for four learner Bash contracts."""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

COURSE = Path(__file__).resolve().parents[1]
TARGETS = {
    "variables": COURSE/"02-bash-scripting"/"01-variables-quoting"/"exercise.sh",
    "status": COURSE/"02-bash-scripting"/"03-status-and-conditions"/"exercise.sh",
    "loops": COURSE/"02-bash-scripting"/"04-loops-and-functions"/"exercise.sh",
    "runner": COURSE/"project"/"run_batch.sh",
}


def verify(mode, script, bash):
    environment = dict(os.environ)
    environment["LE_PYTHON"] = Path(sys.executable).as_posix()
    def invoke(arguments, cwd, extra_env=None):
        settings = dict(environment)
        if extra_env:
            settings.update(extra_env)
        return subprocess.run([bash,str(script),*map(str,arguments)], cwd=cwd,
                              env=settings, capture_output=True, text=True, timeout=15)
    with tempfile.TemporaryDirectory(prefix="le_shell_check_") as directory:
        root=Path(directory)
        if mode == "variables":
            for value in ["hello world", "", "*.csv", "%s $HOME ; echo unsafe"]:
                r=invoke([value],root)
                assert (r.returncode,r.stdout,r.stderr)==(0,f"batch={value}\n",""),"preserve the single argument"
            for args in [[],["a","b"]]:
                r=invoke(args,root)
                assert r.returncode==64 and not r.stdout and r.stderr.strip(),"usage contract"
        elif mode == "status":
            file=root/"input with spaces.txt"; file.write_text("source",encoding="utf-8")
            r=invoke([file],root)
            assert (r.returncode,r.stdout,r.stderr)==(0,"ready\n",""),"readable regular file"
            for target in [root/"missing",root]:
                r=invoke([target],root)
                assert r.returncode==66 and not r.stdout and r.stderr.strip(),"file validation"
            r=invoke([],root)
            assert r.returncode==64 and not r.stdout and r.stderr.strip()
            assert file.read_text()=="source","input changed"
        elif mode == "loops":
            for args,total in [([],0),(["008","2"],10),(["1000000","0"],1000000),(["0000000"],0),(["1"]*100,100)]:
                r=invoke(args,root)
                assert (r.returncode,r.stdout,r.stderr)==(0,f"{total}\n",""),"valid decimal sum"
            for args in [["-1"],["1+2"],[""],["1000001"],["00000000"],["1.2"],["1"]*101,["2","bad"]]:
                r=invoke(args,root)
                assert r.returncode==65 and not r.stdout and r.stderr.strip(),"reject before partial output"
        elif mode == "runner":
            source=root/"input batch.csv";shutil.copyfile(COURSE/"data"/"events.csv",source)
            out=root/"output with spaces"
            r=invoke([source,out],root)
            assert r.returncode==0,"valid runner invocation"
            manifest=json.loads((out/"manifest.json").read_text(encoding="utf-8"))
            assert manifest=={"input_rows":6,"accepted_rows":4,"rejected_rows":2,"event_count":3,"total_cents":3050}
            assert json.loads((out/"run.log").read_text(encoding="utf-8"))["manifest"]==manifest
            assert (out/"error.log").read_text(encoding="utf-8")==""
            r=invoke([root/"missing.csv",out],root)
            assert r.returncode==2,"propagate missing-input status"
            assert json.loads((out/"error.log").read_text(encoding="utf-8"))["event"]=="run_failed"
            assert json.loads((out/"manifest.json").read_text(encoding="utf-8"))==manifest
            assert invoke([],root).returncode==64,"arity"
            assert invoke([source,out],root,{"LE_PYTHON":str(root/"missing-python")}).returncode==127,"missing executable"


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("mode",choices=TARGETS)
    parser.add_argument("--script",type=Path,help="Optional alternative lab script; default is your lesson implementation.")
    parser.add_argument("--bash",default=shutil.which("bash"),help="Bash executable; use Ubuntu Bash for actual course evidence.")
    args=parser.parse_args()
    if not args.bash:
        raise SystemExit("Bash not found. Run this checker in your Ubuntu terminal.")
    script=(args.script or TARGETS[args.mode]).resolve()
    try:
        verify(args.mode,script,args.bash)
    except (Exception,SystemExit) as exc:
        import traceback
        traceback.print_exc(limit=3)
        print(f"FAIL: {args.mode}: {type(exc).__name__}: {exc}")
        return 1
    print(f"PASS: {args.mode}")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
