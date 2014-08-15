# encoding: UTF-8

Vagrant.configure('2') do |config|
  config.vm.box = 'tesora/ubuntu-14.04-amd64'

  config.vm.provider :vmware_workstation do |vm|
    vm.gui = "true"
    vm.vmx["numvcpus"] = 2
    vm.vmx["memsize"] = 1024
    vm.vmx["vhv.enable"] = "true"
  end

  config.vm.define 'ubuntu-14.04' do |c|
    c.vm.box = 'tesora/ubuntu-14.04-amd64'
  
    # install giftwrap from current working directory into the VM
    c.vm.provision 'shell', inline: <<-EOF
      apt-get update
      apt-get install -y python-pip python-dev git
      apt-get install -y build-essential ruby1.9.1-dev
      gem install --no-ri --no-rdoc fpm
      cd /vagrant
      python setup.py install
    EOF
  end

  config.vm.define 'centos-6.5' do |c|
    c.vm.box = 'tesora/centos-6.5-amd64'

    # install giftwrap from current working directory into the VM
    c.vm.provision 'shell', inline: <<-EOF
      rpm -Uvh  http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
      yum upgrade -y
      yum install -y ruby-devel rubygems gcc rpm-build
      gem install --no-ri --no-rdoc fpm
      yum install -y python-setuptools python-pip python-devel git 
      cd /vagrant
      python setup.py install
    EOF
  end

end
