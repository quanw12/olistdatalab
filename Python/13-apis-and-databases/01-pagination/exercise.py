# C13-L01 — HTTP responses, pagination, and bounded extraction
# Implement your own solution below these problem statements.
#
# Implement fetch_all(get_page, start="page1", max_pages=100) -> list.
# get_page(token) returns a dict with items (list) and next (str or None); both keys are required.
# Reject bad page shapes or next values with ValueError.
# Follow tokens in order, concatenate items, stop only on next=None.
# Repeated tokens or exceeding max_pages raise ValueError before an extra request.
# max_pages must have exact positive int type. Do not mutate pages or use a real network.
# See help.md for hints and expected.md for cases.
