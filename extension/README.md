# MediaWiki extension for nb.wtf

This directory contains a MediaWiki 1.39 extension called `NBWTF`. To install the extension:

1. Copy the `NBWTF` directory to your /var/www/html/extensions directory (or wherever your MediaWiki extensions live)
1. Add the following to your `LocalSettings.php` file: `wfLoadExtension('NBWTF');`

The extension registers a `PageSaveComplete` hook that looks for edits to a specific page, `Nb.wtf`.
When that page is saved, the extension makes a "fire and forget" HTTP request to the API of nb.wtf
at `https://nb.wtf/api/v1/on_update`. This kicks off the update logic written in Python in the
`server` part of this repository.

## Development files

The full extension is in the `NBWTF` directory. The other files here, besides this README,
are for developing the extension. They include a docker compose file (`mediawiki.yml`) and
a `LocalSettings.php` file that create a local MediaWiki instance in Docker for testing the
extension.
