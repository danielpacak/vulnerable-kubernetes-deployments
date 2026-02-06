# OWASP/RailsGoat

## Overview

I've modified the [OWASP/RailsGoat](https://github.com/OWASP/railsgoat) web
application a bit. It contains the RCE controller to run commands and see if we
can detect them, for example <http://localhost:3000/rce?cmd=ls%20-l> or <http://localhost:3000/rce_marshal?cmd=ls%20-l>.

Also some Gems are pinned to older versions to demonstrate that we can exploit vulnerable
code execution paths.

In addition, the app is instrumented with Pyroscope SDK for Ruby
so you can see code execution paths as stack traces represented as flame graphs in Pyroscope UI.

## Releases

List of Git branches with different versions of Ruby:

```
git clone git@github.com:danielpacak/railsgoat.git
cd railsgoat
```

* <https://github.com/danielpacak/railsgoat/tree/danielpacak/ruby3.4.1>
* <https://github.com/danielpacak/railsgoat/tree/danielpacak/ruby3.4.1-rails-7.1.0>
* <https://github.com/danielpacak/railsgoat/tree/danielpacak/ruby3.4.5>
* <https://github.com/danielpacak/railsgoat/tree/danielpacak/ruby4.0.1>
* <https://github.com/danielpacak/railsgoat/tree/danielpacak/ruby4.0.1-rails-7.1.0>

List of container images published to DockerHub:

* [docker.io/danielpacak/railsgoat:ruby-3.4.1 (multi-platform)](https://hub.docker.com/repository/docker/danielpacak/railsgoat/tags/ruby-3.4.1/sha256-e5e0c3a62267240815186c66ae95aaae846dd9f8e6d76e1b23ab6802c5a4b4fb)
* [docker.io/danielpacak/railsgoat:ruby-3.4.1-rails-7.1.0 (multi-platform)](https://hub.docker.com/repository/docker/danielpacak/railsgoat/tags/ruby-3.4.1-rails-7.1.0/sha256-dc980837ff01fc0c2e839cd64af25ad17d0b220b282fa13250455318d1cf819d)
* [docker.io/danielpacak/railsgoat:ruby-3.4.5 (multi-platform)](https://hub.docker.com/repository/docker/danielpacak/railsgoat/tags/ruby-3.4.5/sha256-86d9306f7d20fc602b6c361f417afaa5e966b669c2047136b2bdfa408a9761e8)
* [docker.io/danielpacak/railsgoat:ruby-4.0.1 (multi-platform)](https://hub.docker.com/repository/docker/danielpacak/railsgoat/tags/ruby-4.0.1/sha256:fb56ff8efdd54b20d252876c156632a66840d2e9a2ffd5010140010c970d8671)
* [docker.io/danielpacak/railsgoat:ruby-4.0.1-rails-7.1.0 (multi-platform)](https://hub.docker.com/repository/docker/danielpacak/railsgoat/tags/ruby-4.0.1-rails-7.1.0/sha256-e2c3e2368747ada6fdf180e295f69c45d6fcb77617266de98b8aa4378fbe6d4f)

## Vulnerabilities

=== "Ruby 3.4.1 Rails 7.1.0"

    ```
    grype --by-cve docker.io/danielpacak/railsgoat:ruby-3.4.1-rails-7.1.0
    ```

    | NAME          | INSTALLED | VULNERABILITY  | SEVERITY |
    |---------------|-----------|----------------|----------|
    | actionpack    | 7.1.0     | CVE-2024-26143 | Medium   |
    | actionpack    | 7.1.0     | CVE-2024-47887 | Medium   |
    | actionpack    | 7.1.0     | CVE-2024-54133 | Low      |
    | actiontext    | 7.1.0     | CVE-2024-47888 | Medium   |
    | actiontext    | 7.1.0     | CVE-2024-32464 | Medium   |
    | net-imap      | 0.5.4     | CVE-2025-25186 | Medium   |
    | net-imap      | 0.5.4     | CVE-2025-43857 | Medium   |
    | actionmailer  | 7.1.0     | CVE-2024-47889 | Medium   |
    | activerecord  | 7.1.0     | CVE-2025-55193 | Medium   |
    | resolv        | 0.6.0     | CVE-2025-24294 | Medium   |
    | uri           | 1.0.2     | CVE-2025-61594 | Low      |
    | rexml         | 3.4.0     | CVE-2025-58767 | Low      |
    | activestorage | 7.1.0     | CVE-2025-24293 | Critical |

=== "Ruby 4.0.1 Rails 7.1.0"

    ```
    grype --by-cve docker.io/danielpacak/railsgoat:ruby-4.0.1-rails-7.1.0
    ```

    | NAME          | INSTALLED | VULNERABILITY  | SEVERITY |
    |---------------|-----------|----------------|----------|
    | actionpack    | 7.1.0     | CVE-2024-54133 | Low      |
    | actionpack    | 7.1.0     | CVE-2024-47887 | Medium   |
    | actionpack    | 7.1.0     | CVE-2024-28103 | Medium   |
    | actionpack    | 7.1.0     | CVE-2024-26142 | Low      |
    | activerecord  | 7.1.0     | CVE-2025-55193 | Medium   |
    | activestorage | 7.1.0     | CVE-2025-24293 | Critical |
    | actionmailer  | 7.1.0     | CVE-2024-47889 | Medium   |
    | actiontext    | 7.1.0     | CVE-2024-47888 | Medium   |
    | actiontext    | 7.1.0     | CVE-2024-32464 | Medium   |

## SBOM

```
syft scan docker.io/danielpacak/railsgoat:ruby-4.0.1-rails-7.1.0 -o json > railsgoat-ruby401-rails710.sbom.json
```

```
jq '.artifacts[]  | select(.type=="gem") | "\(.name) \(.version)"' railsgoat-ruby401-rails710.sbom.json
```

```
jq '.artifacts[] | select(.name=="actiontext")' railsgoat-ruby401-rails710.sbom.json
```

``` json
{
  "id": "d73207f494f67226",
  "name": "actiontext",
  "version": "7.1.0",
  "type": "gem",
  "foundBy": "ruby-installed-gemspec-cataloger",
  "locations": [
    {
      "path": "/usr/local/bundle/specifications/actiontext-7.1.0.gemspec",
      "layerID": "sha256:a892bf958e0f1ff549909c216fc9c2c0bf6917aa7977dd06565736bdba0a6e97",
      "accessPath": "/usr/local/bundle/specifications/actiontext-7.1.0.gemspec",
      "annotations": {
        "evidence": "primary"
      }
    }
  ],
  "language": "ruby",
  "purl": "pkg:gem/actiontext@7.1.0",
  "metadataType": "ruby-gemspec",
  "metadata": {
    "name": "actiontext",
    "version": "7.1.0",
    "authors": [
      "Javan Makhmali",
      "Sam Stephenson",
      "David Heinemeier Hansson"
    ],
    "homepage": "https://rubyonrails.org"
  }
}
```


## RailsGoat and Pyroscope in Docker

```
docker network create railsgoat
```

```
docker run --rm -d --name pyroscope --network=railsgoat -p 4040:4040 grafana/pyroscope:latest
docker run --rm -d --name railsgoat --network railsgoat \
  -e PYROSCOPE_URL=http://pyroscope:4040 \
  -p 3000:3000 \
  docker.io/danielpacak/railsgoat:ruby-4.0.1-rails-7.1.0 \
    /bin/sh -c "rails db:setup && rm -f tmp/pids/server.pid && bundle exec rails s -p 3000 -b '0.0.0.0'"
```

```
docker stop pyroscope railsgoat
```

## Further Reading

* <https://github.com/OWASP/railsgoat>
