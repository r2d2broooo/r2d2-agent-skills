# R2D2 Agent Skills

A collection of installed, adapted and locally written skill recipes used by coding and research assistants. A skill is a focused instruction file, sometimes accompanied by scripts, references or examples. The collection preserves workflows; it is not a new model runtime or a guarantee that every named integration is installed.

## Skill groups

| Area | Included recipes |
|---|---|
| Research | Holistic stock analysis, trading wiki, forecast-method interpretation and pattern research |
| Engineering | Systematic debugging, verification before completion, test-driven development and source-graph navigation |
| Browser and source inspection | Chrome/CDP workflow and reverse-engineering adapter guidance |
| Knowledge | Book/document-to-skill extraction and on-demand reference structure |
| Design | Frontend guidance, marketing/design taste, diagrams and interactive anatomy examples |

Each directory under `skills/` has a `SKILL.md` describing when to use it. Supporting scripts stay with their recipe, so a reader can inspect both the instruction and the implementation it references.

## How to use the collection

1. Read a selected skill's trigger, scope and prerequisites.
2. Inspect its supporting scripts and references.
3. Install or link that selected directory into your assistant's supported skill directory.
4. Configure the named external tools separately.
5. Invoke the skill for an appropriate task and verify its output.

Start with one relevant skill rather than loading the entire collection into every prompt. Research skills may expect the separate trading/data workspace. Browser skills need a local browser setup. REA and Graphify recipes reference their own upstream tools. Design examples are reference assets, not deployed applications.

## Authorship and licensing

This is a mixed-provenance collection. Some recipes and integration code were written locally; others were installed or adapted from upstream projects. [UPSTREAMS.md](UPSTREAMS.md) records the known origins. Included MIT/Apache notices remain with the material they cover. Public access does not transfer authorship or apply one blanket license to unrelated third-party files.

Retain the applicable notices when reusing a skill, and check the individual origin/license where one is not specified. Model CLIs, hosted plugins, subscriptions and accounts are dependencies; their executables and credentials are not distributed here.

## Checks and limits

```bash
python3 check.py
```

The checks parse executable source formats and JSON where applicable. They do not run every skill, call models, open accounts or certify generated diagrams/research. Example PDFs illustrate upstream design output and have been checked separately for metadata/content that could identify the source workstation. No private chats, books, account screenshots or browser profiles are included.

The shared workflow uses independent provider identities and reviews only when requested. Installing this repository does not schedule a team review, send a message or enable automatic updates.

## Privacy, provenance and updates

This repository is a sanitized source export. No provider credentials, personal contact information, configured IP addresses, private conversations or runtime databases are included. Example hostnames and local environment variables are intentional. Keep newly generated account data and captures outside version control.

A source manifest records exported files. Local adaptations and third-party material retain their own provenance/notices; public visibility does not apply a new blanket license to every file. Related repositories and the manual update process are listed in the [workspace catalogue](https://github.com/r2d2broooo/r2d2-workspace-catalog).

Updates are made only on explicit request. Cloning does not enable an automatic sync, scheduled publication or Git push.
