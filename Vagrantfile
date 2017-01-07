# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define :tiacos do |tiacos_config|
	  # Every Vagrant virtual environment requires a box to build off of.
	  tiacos_config.vm.box = "ubuntu/xenial64"

	  # required by couchbase-cli
	  tiacos_config.ssh.shell = "export LC_ALL=\"en_US.UTF-8\""
	  tiacos_config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

	  # Create a private network, which allows host-only access to the machine
	  # using a specific IP.
	  tiacos_config.vm.network :private_network, ip: "192.168.56.101"

          # Mapping folders
	  tiacos_config.vm.synced_folder "labs/", "/home/ubuntu/labs"

	  tiacos_config.vm.provider :virtualbox do |vb|
	    vb.customize ["modifyvm", :id, "--memory", "2048"]
	  end
	  
	  tiacos_config.vm.provision :shell, :path => "install_puppet.sh"

	  #puppet config
	  tiacos_config.vm.provision "puppet" do |puppet|
	    puppet.module_path = "puppet/modules"
	    puppet.manifests_path = "puppet/manifests"
	    puppet.manifest_file = "."
	    puppet.options = "--environment dev"
	  end
   end
end

