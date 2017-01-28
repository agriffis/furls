furls
=====

furls is an HTTP file server, designed to serve files on unique URLs for
persistence, tracking and versioning.

**persistence**: once a file is uploaded and an URL generated, it persists
unless the user removes it or disables its URL. This can be helpful when a
deployed application depends on some large static assets that would be unwieldy
to include in the git repository and deployed instance.

**tracking**: furls keeps simple analytics for each file.

**versioning**: the URL scheme includes an optional version component, so an URL
can either be pinned to a version or allowed to track the latest upload for the
file.

status
------

Nothing here works yet, just getting started.

plans
-----

Rough steps:

 1. Build an MVP that uses purely the Django admin for file uploads and URL
    creation, i.e. no other user interface.
 2. Add an API for a separate front-end web app.
 3. Add a command-line client, should use the API for authenticated uploads.

Additionally would like to use this project as a vehicle for some experiments,
especially:

  * approaches to auth with front/back split
  * latest django on python 3
  * dev directly on docker instead
    of [vagrant-docker](https://www.vagrantup.com/docs/docker/index.html)
    as [we're doing in other projects](https://github.com/scampersand/sonos-back/blob/master/Vagrantfile)
  * deploy as containers, for example
    to [Heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime)
  * continuous deployment

though one of the obvious places to deploy this is Dreamhost since it can host
both Django and file serving in existing aaccount, and that precludes deploying
as containers.

legal
-----

Copyright 2017 [Scampersand LLC](https://scampersand.com)

Released under the [MIT license](https://github.com/scampersand/furls/blob/master/LICENSE)
