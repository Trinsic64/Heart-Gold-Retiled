# Release checklist

Use GitHub Releases for versioned public downloads while keeping the same files in the repository for transparency.

1. Confirm the patch was produced from a clean, legally obtained ROM dump.
2. Test the patch from start to finish on a fresh copy of the compatible source revision.
3. Run the content-safety workflow and inspect the complete staged file list.
4. Confirm no ROM, save, executable, DSPRE workspace, extracted ROM, or secret is present.
5. Recompute SHA-256 hashes for the patch and map archives.
6. Update `README.md`, `checksums.sha256`, and the version number together.
7. Create a tag such as `v1.0.0` and a GitHub Release.
8. Attach only the `.xdelta` and/or `.bps` patches, optional map archives, and `checksums.sha256`.
9. Document the compatible source ROM region/revision and its SHA-256 when known; do not upload the source ROM.
10. Download the published assets once and verify their hashes.

Recommended release notes should clearly state the unfinished areas, important tile fixes, known glitches, compatible source revision, patch SHA-256, and feedback link.
