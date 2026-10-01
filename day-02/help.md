# Day 2 hints

Open only the TODO you are stuck on. Type each line yourself and track what each variable contains.

## TODOs 1 and 2: empty collections

~~~python
temperatures = []
cities = set()
~~~

`[]` creates an empty list. `set()` creates an empty set; `{}` creates an empty dictionary.

## TODO 3: visit each row

~~~python
for row in rows:
    city = row["city"]
    temperature_c = row["temperature_c"]
~~~

`row` is a temporary variable. Each iteration assigns the next dictionary in `rows` to it.

## TODO 4: collect values

Place these **inside** the loop, at the same indentation as the two lookup lines:

~~~python
cities.add(city)
temperatures.append(temperature_c)
~~~

The set keeps each city name once. The list keeps every temperature because each is an observation used in the calculation.

## TODO 5: calculate statistics

Place this **after** the loop, at the function body's indentation level (four spaces):

~~~python
lowest_temperature = min(temperatures)
highest_temperature = max(temperatures)
average_temperature = round(sum(temperatures) / len(temperatures), 1)
~~~

The list now contains five numbers. Their sum divided by their count gives the mean.

## TODO 6: return the report

~~~python
return {
    "row_count": len(rows),
    "cities": sorted(cities),
    "temperature_min_c": lowest_temperature,
    "temperature_max_c": highest_temperature,
    "temperature_avg_c": average_temperature,
}
~~~

`sorted(cities)` produces an ordered list so the output is consistent.

## Troubleshooting

| Error or symptom | Common cause | Fix |
|---|---|---|
| `NameError: temperatures is not defined` | Missing list or wrong scope | Create it inside `summarize_weather`, before `for` |
| `KeyError: ...` | Misspelled key | Use `"city"` and `"temperature_c"` |
| `TypeError: 'NoneType' object is not subscriptable` | Function does not return a dictionary | Complete TODO 6 and remove `pass` |
| `IndentationError` | Inconsistent block indentation | Use four spaces; do not mix tabs and spaces |
| Incorrect average | Append outside the loop, or missing division | Check TODOs 4 and 5 |

## Trace by hand

First iteration:

~~~python
row = {"city": "Hanoi", "temperature_c": 31.2}
~~~

After collecting the values:

~~~python
cities        # {"Hanoi"}
temperatures  # [31.2]
~~~

The second iteration adds `"Da Nang"` and `30.1`. After five iterations, the list has five temperatures and the set has three city names.
