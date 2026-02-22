# PR Review - Release notes auto-generator (by Vikram Singh)

## Reviewer: Neha Sharma
---

**Overall:** Good foundation but critical bugs need fixing before merge.

### `releaseNotesGenerator.ts`

> **Bug #1:** Commit message parsing regex does not handle multi-line messages and only captures first line
> This is the higher priority fix. Check the logic carefully and compare against the design doc.

### `commitParser.ts`

> **Bug #2:** Version sorting treats 1.10.0 as less than 1.9.0 because of string comparison
> This is more subtle but will cause issues in production. Make sure to add a test case for this.

---

**Vikram Singh**
> Acknowledged. I have documented the issues for whoever picks this up.
