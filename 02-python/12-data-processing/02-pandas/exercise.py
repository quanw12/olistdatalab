# C12-L02 — pandas joins, types, and trustworthy totals
# Implement your own solution below these problem statements.
#
# Implement region_totals(orders, cities) -> pandas.DataFrame.
# orders columns: city, amount_cents. cities columns: city, region.
# Reject null city keys in either input, duplicate dimension city keys, and unmatched order cities with ValueError.
# Amounts are already validated integer cents; regions are nonnull strings.
# Return columns ['region','total_cents'], summed by region, sorted by region with a fresh index.
# Do not mutate inputs. Empty orders return an empty DataFrame with those columns.
# See help.md for hints and expected.md for cases.
