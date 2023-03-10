test-copy-file
=========

This role allows to test copy-file module

Role Variables
--------------

| Name         | Default    | Description |
|--------------|------------|-------------|
|copy_file_path| ~/example.txt|Path to the file being created|
|copy_file_content| Created with wowpetr.devops1.create_file ansible collection\n|Content of the file|


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: wowpetr.devops1.test-copy-file }

License
-------

MIT

Author Information
------------------

Petr Losev (@wowpetr)
