import sublime, sublime_plugin, os, subprocess
PLUGIN_DIR = os.path.abspath(os.path.dirname(__file__))

class ProcessDataBagItemMixin(object):
    def str(self, s):
        try:
            # Python 2
            return unicode(s, "utf_8")
        except NameError:
            # Python 3
            return str(s, "utf_8")

    def run(self, edit):
        repository_root = self.view.window().folders()[0]
        secret_file = os.path.join(repository_root, "data_bag_key")

        # Read data_bag_key
        if not os.path.exists(secret_file):
          settings = sublime.load_settings("ChefEncryptedDataBag.sublime-settings")
          secret_file_setting = settings.get("encrypted_databag_secret", "encrypted_databag_secret")
          secret_file = os.path.join(repository_root, secret_file_setting)

        # Get content
        region_all = sublime.Region(0, self.view.size())
        data = self.view.substr(region_all)

        # Encrypt / Decrypt
        processed_data = self.process(data, secret_file)
        self.view.replace(edit, region_all, processed_data)

    def process(self, data, secret_file):
        raise "Please override #process"

    def run_script(self, script_name, data, secret_file):
        settings = sublime.load_settings("ChefEncryptedDataBag.sublime-settings")
        ruby = settings.get("ruby", "ruby")
        pretty_json = settings.get("pretty_json", "pretty_json")

        script_path = os.path.join(PLUGIN_DIR, script_name)
        cmd = [ruby, "--encoding", "utf-8", script_path, secret_file, pretty_json]

        proc = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        stdout, stderr = proc.communicate(data.encode("utf_8"))

        returncode = proc.wait()
        if returncode != 0:
            sublime.error_message(self.str(stderr))
            raise
        return self.str(stdout)

class EncryptDataBagItemCommand(ProcessDataBagItemMixin, sublime_plugin.TextCommand):
    def process(self, data, secret_file):
        return self.run_script("chef_encrypt_databag_item.rb", data, secret_file)

class DecryptDataBagItemCommand(ProcessDataBagItemMixin, sublime_plugin.TextCommand):
    def process(self, data, secret_file):
        return self.run_script("chef_decrypt_databag_item.rb", data, secret_file)
