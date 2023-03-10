# wowpetr.devops1

An Ansible Collection of modules that was created for learning purposes.

## Supported Versions of Ansible
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.14**.

## Included content
### Modules
Name | Description
--- | ---
create_file|Create text file with any content.

## Installing this collection

You can install the ``wowpetr.devops1`` collection with the Ansible Galaxy CLI after cloning this repository:

    ansible-galaxy collection build
    ansible-galaxy collection install wowpetr-devops1-1.0.0.tar

### Using this collection
After installation you can use this command to test the `create_file` module with [test_module](./playbooks/test_module.yml) playbook (supplied with this collection):

    ansible-playbook wowpetr.devops1.test_module

## Modules documentation
You can read modules documentation using `ansible-doc`, providing that the collection is installed:

    ansible-doc create_file

License
-------

MIT

Author Information
------------------

Petr Losev (@wowpetr)