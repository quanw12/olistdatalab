# DE14 assignment

Create project/dbt/models/properties.yml with descriptions, unique/not_null on latest id, accepted_values on op and non-null mart fields. Create tests/assert_mart_reconciles.sql comparing mart counts/totals to active latest state. Test that deletes do not count as active. Run build/test. In an isolated project copy, alter a mart total or duplicate a key, demonstrate semantic test failure, restore and pass.

## Deliverables

Properties, singular tests and notes.md with failure/repaired pass.

## Reflection

Does unique_key replace a uniqueness assertion?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

