# Help — HTTP responses, pagination, and bounded extraction

## First hint

Keep a seen-token set and a count before every request.

## Detailed approach

Loop while token is not None. Before calling get_page, reject seen tokens or count >= max_pages; then add the token, increment count, fetch/validate and extend output. Empty items may coexist with a next token. Do not retry here; that belongs in a separate wrapper.

## Troubleshooting

Stopping on an empty page can miss data. Adding a token to seen after a recursive call can fail to detect cycles in time.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.
