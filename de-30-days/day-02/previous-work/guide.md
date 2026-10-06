# Day 2 — Python basics through a weather report

## Day 1 review

Your submitted counts were correct:

~~~text
accepted: 5
rejected: 5
~~~

The five rejected rows matched the data contract, and no error blocked the exercise. Functions, syntax, and Python logic were still unclear, so Day 2 slows down to practise them before moving to JSON, APIs, and databases.

## Today's goal

Write a function that summarizes five clean weather records:

~~~text
rows: 5
cities: Da Nang, Hanoi, Ho Chi Minh City
temperature min: 29.8 C
temperature max: 33.4 C
temperature avg: 31.3 C
~~~

This is a small **transform** step: clean data goes in, a summary comes out.

## Learning order

1. Read [the Python lesson](lesson.md), sections 1–7.
2. Open `exercise.py`. Read `WEATHER_ROWS` and `print_summary` first.
3. Complete `summarize_weather` one TODO at a time. No pandas or new libraries are needed.
4. If a TODO takes more than 15 minutes without progress, read its section in [help.md](help.md).
5. Run from PowerShell in `C:\DE Courses\day-02`:

~~~powershell
python exercise.py
~~~

6. Compare the result with the expected output above.

## Completion checklist

- [ ] Explain the function's input and return value.
- [ ] Explain why temperatures use a list and cities use a set.
- [ ] Trace `for row in rows` step by step.
- [ ] Produce the five report lines.
- [ ] Remove `pass` from `summarize_weather` after adding real code.

## Git checkpoint

When the result is correct, run from `C:\DE Courses`:

~~~powershell
git status
git add day-02
git commit -m "feat(day-02): add weather summary exercise"
git push
~~~

Commit after writing and understanding the exercise yourself. A new branch is not required for this personal learning exercise.

## Extra practice

Return to `C:\DE Courses\day-01\clean.py` and explain:

1. What does the `pass` at the end of the loop do?
2. Why can `clean` be treated as a dictionary after `if clean is None: ... continue`?
3. Why is `str(clean["city"])` unnecessary here?

You do not need to change Day 1 yet. Send your reasoning for review first.

## Send after finishing

1. Full output from `python exercise.py`.
2. Your `summarize_weather` function body.
3. One sentence explaining how `return` differs from `print`.
