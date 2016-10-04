# ChefEncryptedDataBag

Sublime Text 2/3 Plugin to encrypt/decrypt [chef](https://www.chef.io/chef/) encrypted data item.

# Requirements

- ruby >= 1.9
- chef gem 11.12.4 tested

# Settings

Open menu item `[Sublime Text 2/3]-[Preferences]-[Package Settings]-[ChefEncryptedDataBag]-[Settings - User]`.

To see default settings, open menu item `[Sublime Text 2/3]-[Preferences]-[Package Settings]-[ChefEncryptedDataBag]-[Settings - Default]`.

# Usage

1. Open chef repository directory that have `data_bag_key` file.
2. Open encrypted/plain data bag item (JSON).
3. Open command palette (`command + shift + p`) and run `Chef: Encrypt/Decrypt data bag item`

Alternatively:

1. Set encrypted_databag_secret in your Settings to point to your data bag secret.
2. Open command palette (`command + shift + p`) and run `Chef: Encrypt/Decrypt data bag item

# License

MIT License.
Copyright 2015-2016 labocho.
