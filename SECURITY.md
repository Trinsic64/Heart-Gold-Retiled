# Security and content safety

This repository intentionally distributes only an xDelta patch, screenshots, documentation, and mapping resources. It must not contain complete ROM images, save files, executables, secrets, or DSPRE/extracted-ROM projects.

## Verify releases

Compare downloaded files with [checksums.sha256](checksums.sha256). A mismatched checksum means the file is not the version documented by this repository; delete it and download it again from the official repository page.

## Reporting a problem

For an accidentally published ROM, extracted game data, credential, or other sensitive file, use GitHub's private **Security → Report a vulnerability** option if it is enabled. Do not repost or attach the sensitive content.

For an ordinary broken link or incorrect checksum, open a public issue without attaching prohibited files.

## Maintainer response

If prohibited or sensitive content is discovered, maintainers should remove public access, rotate any exposed credential, purge the affected Git history when necessary, regenerate release artifacts, and publish new checksums before restoring distribution.

