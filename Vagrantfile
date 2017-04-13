# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false

  config.vm.define "naaf" do |naaf|

  end

    config.vm.provider "virtualbox" do |v|
      v.customize [
        "modifyvm", :id,
        "--memory", "1024",
        "--cpus",   "2"
      ]
    end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update

    sudo apt-get --assume-yes install python-virtualenv python3-pip

    sudo apt-get --assume-yes install libxss1 libappindicator1 libindicator7
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome*.deb
    sudo apt-get --assume-yes install -f

    sudo apt-get --assume-yes install xvfb -f

    sudo apt-get --assume-yes install unzip
    wget -N http://chromedriver.storage.googleapis.com/2.20/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver

    sudo mv -f chromedriver /usr/local/share/chromedriver
    sudo ln -sfn /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -sfn /usr/local/share/chromedriver /usr/bin/chromedriver

    cd /vagrant/
    ./setup.sh

    echo "
    alias reload='source /home/vagrant/.profile'
    alias cd..='cd ..'
    alias ..='cd ..'

    cd /vagrant/
    . virtualenv/bin/activate
    " >> /home/vagrant/.profile
  SHELL
end
