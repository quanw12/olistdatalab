# Help — Grain, dimensions and historical meaning

## First hint

Separate source version history from the analytical current-state fact.

## Detailed approach

Sketch the three grains on paper. Store source id/version independently of dimension surrogate keys. Use event_at >= valid_from AND (valid_to IS NULL OR event_at < valid_to). Count matches per event with a LEFT JOIN so missing dimension matches remain visible. Group and fail on counts other than one. Decide how to represent an unknown customer; do not silently drop its revenue.

## Troubleshooting

A Type 2 history is not produced just by adding valid_from. A unique business key would prevent multiple historical rows. An inclusive BETWEEN can double-match a boundary.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

