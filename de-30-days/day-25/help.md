# Day 25 — Analytics: turn clean data into an honest report


1. Read both CSVs, confirm8 observations and4 configured cities, then parse timestamps as UTC. For this fixture every city shares Asia/Ho_Chi_Minh; convert before taking local dates.
2. Aggregate observations per city, merge onto configured cities, and fill only observation_count with0. Hue's measurement statistics stay missing.
3. Group by city and local_date for daily_summary; there are five observed groups. An overall daily summary has two rows, a different grain.
4. Make one figure at a time. For the trend plot, group by city and sort observed_at. Format x-axis labels to include local time/zone, rotate if needed, and add a legend.
5. Reconcile the sum of observation_count with8. Compare averages before rounding; round only output presentation.
6. In report.md call the data a fixed demo. A screenshot of a chart does not replace the script and input needed to reproduce it.
