# HTTP responses, pagination, and bounded extraction

Original Python-for-DE extension. [Source reference](https://requests.readthedocs.io/en/latest/user/quickstart/).

## Concept and purpose

An HTTP response has a status, headers and a body. A request can time out, return an error status, or return a body that violates your schema. Treat these as distinct failures.

With requests, session.get(url, timeout=(3, 10)) sets connection/read timeout behavior, response.raise_for_status() rejects unsuccessful statuses, and response.json() parses JSON. A read timeout is not a single overall job deadline. Authentication normally uses headers or a session; read credentials from the environment rather than source files.

Pagination splits a result into pages. Follow the API's documented next token, stop at an explicit terminal marker, and guard against repeated tokens and unbounded page counts. Never assume an empty items array means there are no further pages.

The exercise injects a page-fetching function with an already-parsed response. This separates HTTP details from pagination logic and keeps the checker offline. A real adapter must separately validate allowed hosts if it follows server-supplied URLs.

## Syntax example

~~~python
pages={
    "first":{"items":[1,2],"next":"second"},
    "second":{"items":[],"next":None},
}
def get_page(token):
    return pages[token]
print(get_page("first")["next"])
~~~

## Trace

The next token is second. The caller still needs to fetch that page before deciding the stream is finished.

## DE connection

A pipeline that fetches only the first page can look healthy while silently omitting most records.

Use [exercise.py](exercise.py) for the exact input/output contract.
