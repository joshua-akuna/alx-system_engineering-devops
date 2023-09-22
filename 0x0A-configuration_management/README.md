# 0x0A. Configuration management
## Resources
### Read or watch
[Into to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)

[Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html) (check "Resource types" for all manifest types in the left menu)

[Puppet's Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)

[Puppet lint](http://puppet-lint.com/)

[Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled

### Install *puppet*
> apt-get install -y ruby=1:2.7+1 --allow-downgrades

> apt-get install -y ruby-augeas

> apt-get install -y ruby-shadow

> apt-get install -y puppet

### Install *puppet-lint*
> gem install puppet-lint

## Tasks
### 0. Create a file
Using Puppet, create a file in */tmp*.
Requirements:
* File path is */tmp/school*
* File permissions is *0744*
* File owner is *www-data*
* File group is *www-data*
* File contains *I love Puppet*

**File**: [0-create_a_file.pp](https://github.com/joshua-akuna/alx-system_engineering-devops/blob/master/0x0A-configuration_management/0-create_a_file.pp)

### 1. Install a package
Using Puppet, install *flask* from *pip3*
Requirements:
* Install *flask*
* Version must be *2.1.0*

**File**: [1-install_a_package.pp](https://github.com/joshua-akuna/alx-system_engineering-devops/blob/master/0x0A-configuration_management/1-install_a_package.pp)
