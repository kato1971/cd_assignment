[![Run Tests and Deploy to Digital Ocean Droplet](https://github.com/kato1971/cd_assignment/actions/workflows/run-tests.yml/badge.svg)](https://github.com/kato1971/cd_assignment/actions/workflows/run-tests.yml)

# CD Assignment

## Three components of my solution

1. **Github Actions**:
    - GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows me to automate my build, test, and deployment pipeline. I can create workflows that build and test every pull request to my repository, or deploy merged pull requests to production.
    - With Github Actions I've deployed my Flask app to DigitalOcean
2. **Digital Oceon**:
    - DigitalOcean is a cloud computing vendor with data centers worldwide that offers an infrastructure as a service (IaaS) platform for software developers.
    - On DigitalOcean I created a droplet. DigitalOcean Droplets are Linux-based virtual machines (VMs) that run on top of virtualized hardware.
3. **SSH**:
    - SSH or Secure Shell is a network communication protocol that enables two computers to communicate  and share data.
    - I used SSH to communicate between Github and DigitalOcean


## Three promblems I ancountered along the way

1. **First problem**: 
    I had a hard time setting up a droplet on Digital Ocean because I didn't have a credit card or paypal account. For that I created a paypal account and I was able to set up a droplet.

2. **Second problem**:
    I was having trouble pushing my repository on Github using Git from the command line. I got the message that it was not a git repository. I used the `git init` command for that and that solved the problem.

3 **Third problem**:
    For some reason there was a wrong shh-key in the known-hosts file. I got the message ssh: handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain.
    I removed the github ssh key from the known_hosts file and put the correct ssh key in it. That solved the problem.

> It's usually not a good idea to give continuous deployment pipelines root access to your server, so I have added a user