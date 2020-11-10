bcrisp4.k3s.install
=========

Install the k3s (lightweight kubernetes) binary

Role Variables
--------------

| Variable                | Default                                     | Description                                                                                                                                                                                                                    |
|-------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| k3s_channel             | "stable"                                    | The release channel to use when downloading k3s.   The role will choose the latest release in the specified channel, as described here: https://update.k3s.io/v1-release/channels  This value is ignored if k3s_version is set |
| k3s_version             |                                             | The version of k3s to install  Takes precedence over k3s_channel                                                                                                                                                               |
| k3s_bin_dir             | "/usr/local/bin"                            | The directory that the k3s binary should be installed to                                                                                                                                                                       |
| k3s_bin_owner           | "root"                                      | The user that should own the k3s binary                                                                                                                                                                                        |
| k3s_bin_group           | "root"                                      | The group that should own the k3s binary                                                                                                                                                                                       |
| k3s_bin_mode            | "u=rwx,go=rx" (0755)                        | The file permissions that should be applied to the k3s binary                                                                                                                                                                  |
| k3s_allow_replace_bin   | false                                       | Should the role replace any existing k3s binary found at `$k3s_bin_dir/k3s` ?                                                                                                                                                  |
| k3s_github_url          | "https://github.com/rancher/k3s"            | The URL of the k3s GitHub project. Used as the base URL for k3s binary downloads.                                                                                                                                              |
| k3s_release_channel_url | "https://update.k3s.io/v1-release/channels" | The URL of the API endpoint used to query k3s release channels. 

Example Playbooks
----------------

### Install the current stable release of k3s

```yaml
- hosts: k3s_hosts
  tasks:
    - import_role:
        name: bcrisp4.k3s.install
```

### Install a specific version of k3s

```yaml
- hosts: k3s_hosts
  vars:
    k3s_version: v1.19.3+k3s2
  tasks:
    - import_role:
        name: bcrisp4.k3s.install
```

### Install the latest release of k3s to a custom location, replacing any existing k3s binaries

```yaml
- hosts: k3s_hosts
  vars:
    k3s_channel: latest
    k3s_bin_dir: /some/bin/dir
    k3s_allow_replace_bin: yes
  tasks:
    - import_role:
        name: bcrisp4.k3s.install
```


License
-------

GNU General Public License v2.0 or later

Author Information
------------------

Ben Crisp (ben@thecrisp.io)
