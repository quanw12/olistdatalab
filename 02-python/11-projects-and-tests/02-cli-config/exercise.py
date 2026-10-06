# C11-L02 — CLI options, configuration, and environments
# Implement your own solution below these problem statements.
#
# Implement parse_args(argv) -> argparse.Namespace.
# --input is required. --limit is an integer defaulting to 100; zero/negative values must cause SystemExit through parser.error.
# Implement load_settings(path): read UTF-8 JSON, require an object with nonblank string source and exact positive integer batch_size.
# Invalid schema raises ValueError. Return only {'source': stripped_source, 'batch_size': value}; ignore additional fields without logging them.
# See help.md for hints and expected.md for cases.
