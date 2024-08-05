# nb.wtf link shortener/go links

This repo provides two sub-repos, that together power the [Noisebridge](https://www.noisebridge.net/wiki/Noisebridge)
link shortener service at https://nb.wtf.

## Overview

[This page](https://www.noisebridge.net/wiki/Nb.wtf) on the Noisebridge wiki contains a table that maps "shortcodes"
or "slugs" to URLs. The URLs can either be a link in the wiki, where the entry can be referenced in wiki code by its
wiki link name (aka `[[About]]`), or a full http/https URL.

Anyone who can edit the wiki can add/remove/modify shortcodes using this page. When it is updated, the service
at https://nb.wtf should be updated within seconds, and the link becomes available at https://nb.wtf/shortcode.

## Server

The directory `server` contains the code for the Python Flask code that handles two things:

1. Reading the wiki page and updating the shortcode -> URL mappings when the `on_update` API method is called.
1. Responding to GET requests for shortcodes and serving 302 redirects.

The server is currently hosted for free on [Fly.io](https://fly.io/) and its administrator is
[Travis](mailto:audiodude@gmail.com).

The mappings are stored in a free [MongoDB Cloud](https://www.mongodb.com/products/platform/cloud) instance.
The URL of the wiki page and the base URL of the wiki are configurable in the `.env` file (not included).

## Extension

See the README.md in the extension sub directory for more information on how to install the extension.

Basically, the extension provides an "on page save" hook that simply calls the `on_update` API method of
the server at nb.wtf. The URL of the server is hardcoded into the extension. This keeps the wiki page
and the server in sync.

### More information

For more information, contact [https://www.noisebridge.net/wiki/User:Audiodude](Travis/audiodude).
