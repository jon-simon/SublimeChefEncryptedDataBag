#!/usr/bin/env ruby

begin
  require 'chef/encrypted_data_bag_item'
rescue LoadError
  $stderr.puts "LoadError: `chef` gem is not installed.\n#{$!.backtrace.join("\n")}"
  exit 1
end
require 'json'

secret = Chef::EncryptedDataBagItem.load_secret ARGV.first
data = JSON.load STDIN.read
encrypted_data = Chef::EncryptedDataBagItem.encrypt_data_bag_item(data, secret)
if ARGV.last == 'decrypt'
  output = encrypted_data.to_json
else
  output = JSON.pretty_generate(encrypted_data)
end
STDOUT.write output
