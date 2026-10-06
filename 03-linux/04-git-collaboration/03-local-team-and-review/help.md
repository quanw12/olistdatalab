# Help — Local remotes, pull requests and review evidence

## First hint

Separate receiving history from integrating history.

## Detailed approach

~~~bash
mkdir -p "$LE_LAB_ROOT/git/team"
git init --bare --initial-branch=main "$LE_LAB_ROOT/git/team/origin.git"
git clone "$LE_LAB_ROOT/git/team/origin.git" "$LE_LAB_ROOT/git/team/alice"
git clone "$LE_LAB_ROOT/git/team/origin.git" "$LE_LAB_ROOT/git/team/bob"
~~~
Do this only when those named destinations are new. An empty-remote warning is expected initially. Alice's first main push establishes history; Bob may then need to create its tracking main. Use git -C <clone> to operate on a specific clone without losing directory context. Local remote paths do not send work to GitHub. Review the full diff before merging.

Configure each clone locally, then create Alice's initial history:

~~~bash
for person in alice bob; do
    clone="$LE_LAB_ROOT/git/team/$person"
    git -C "$clone" config user.name "$person"
    git -C "$clone" config user.email "$person@example.test"
    git -C "$clone" config commit.gpgsign false
done
cd "$LE_LAB_ROOT/git/team/alice"
printf '# Pipeline lab\n' > README.md
git add -- README.md
git commit -m 'docs(lab): create project overview'
git push -u origin main
cd "$LE_LAB_ROOT/git/team/bob"
git fetch origin
git branch --list
~~~

For the fresh empty clone in this lab, there is no committed local main yet. Create it with `git switch -c main --track origin/main`. If main already exists, use `git switch main` followed by `git pull --ff-only` instead. Continue:

~~~bash
git switch -c feature/change
~~~

Edit README.md to add your improvement, then:

~~~bash
git diff
git add -- README.md
git commit -m 'docs(lab): explain recovery behavior'
git push -u origin feature/change
cd "$LE_LAB_ROOT/git/team/alice"
git fetch origin
git diff main...origin/feature/change
git status
~~~

Alice's working README stays unchanged after fetch. Use that evidence in your explanation. Write review.md and pr.md in this lesson's course folder so they can be committed with your notes; the practice clones themselves stay outside the course repository.

## Troubleshooting

An empty clone has no branch history yet. A bare remote's HEAD must name main to avoid confusing clone defaults. 'Already exists' means inspect/reuse the lab rather than recursively removing it.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
