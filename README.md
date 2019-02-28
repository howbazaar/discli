# Discourse Helper

This is a simple helper utility to get files in and our of discourse for local editing.

To get started you need an api key from the discourse instance:

TODO: insert link about generating api key

Next step is to call init with the key

```bash
dislci init <discourse url> <discourse username> <api key>
```

This writes a file in `~/.local/share/discli`. You only need to do this once (unless you change the api key).

Next is to get a topic. For example, grabbing https://discourse.jujucharms.com/t/agent-introspection/117.

```bash
$ discli get 117
```

This stashes some metadata about the post in .discli in the working directory, and creates a file `117-agent-introspection.md`.

You can edit this, and push changes.

```bash
$ discli put 117
# or
$ discli put 117-agent-introspection.md
```

If anyone else has changed the post while you were editing, the put will fail. Future work may deal with merging and conflict resolution.
The local file is also removed once put back.
