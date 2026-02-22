# FINSERV-4267: Investigate release notes generator outputting malformed changelog

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 30 · **Story Points:** 8
**Reporter:** Meera Sharma (Release Lead) · **Assignee:** You (Intern)
**Due:** End of sprint (Friday)
**Labels:** `backend`, `python`, `tooling`, `release`
**Task Type:** Code Debugging

---

## Description

The release notes generator parses commit messages (Conventional Commits format) and generates a changelog. The output has several issues.

**DEBUGGING task — no hint comments. Investigate from symptoms.**

## Symptoms

- `feat:` commits appear under the "Bug Fixes" section
- `fix:` commits appear under the "Features" section
- Breaking changes (commits with `BREAKING CHANGE:`) are completely missing from output
- Version bump logic: patch release shows as major, major shows as patch
- Commits with scopes `feat(api):` lose the scope in the output

## Acceptance Criteria

- [ ] Root cause found and fixed
- [ ] feat/fix/breaking mapped to correct sections
- [ ] Version bumps are correct
- [ ] All unit tests pass
