# Becoming a CNA Ninja 1: Why Containers, why now

## What's in it for me

We are going to take you, the humble reader from CNA zero, to CNA hero. We will introduce every feature and topic thoroughly, explain why it's needed and show it in action with practical, follow-along examples.

Over the course of this series we are going to build an application and move it, just as a developer would from inception to production readiness using Docker, Kubernetes and fully automated releases using CI/CD pipelines. Using advanced K8s primitives like Horizontal Pod Autoscaling, StorageClasses, LoadBalancers, StatefulSets and even dabbling in service meshes like Istio for A/B testing, tracing and canary releases (because let's be honest, everyone and their grandma will want to use our app and it just won't do if it's unreliable).

Sound complex? Well, you're in the right place then, because while it may seem daunting to begin with - following along with this series will explain everything clearly, justify and demonstrate its need in our kickass app.

Without further ado, let's get to making you a CNA Ninja!

## What is a container

A container, simply put, is a collection of just enough libraries, binaries and code to run your chosen application all held together in a tarball. They are a built on top of a [combination of a few linux primitives](https://ericchiang.github.io/post/containers-from-scratch/) namely; `namespaces`, `cgroups` and `chroot` the provide process, resource and filesystem isolation respectively.

Even though containers are the flavour of the moment they've been around in one form or another since the turn of the millennium through BSD Jails, Solaris Containers, OpenVZ and LXC which were all different interpretations of the same concept.

While most of us are (I hope) familiar with kernel-mode virtualization (VMs), OS-level virtualization for process and network isolation might be new to those of us who have been in the VM space for some time. So to better understand containers and where they fit in, let's start at the start - why do we want to use containers in the first place?

This can seem opaque in the beginning as these are challenges that a VM admin/sysadmin typically wouldn't have had to deal with and are generally specific to development, but you will no doubt be able to relate to some of the challenges presented by typical application development methods. With that said, let's explore the reasons behind the container movement. As far as I see it there are five main drivers behind the containerization of applications:

* Sharing a common kernel between applications, which reduces overhead
* While sharing a kernel, libraries are kept separate between containers greatly simplifying dependency chains
* Simplification of the application development and provisioning cycle because everything needed to run the app is "in a box" that is a known good.
* Rapid auto-scaling and scale-to-zero capabilities
* Perfect integration with Continuous Development / Continuous Integration pipelines

Some of the above may seem a little abstract at the moment, but we will get into them over the course of this learning series. Before we dive into the specifics of the above, let's take a look at how containers differ at an architectural level from VMs.

I made up this handy-dandy diagram that illustrates the levels of separation afforded by a vm compared to a container.

![Difference between containers and VMs](img/Containers-VMs.png)
_(Figure 1) Architectural differences between VMs and containers_

You will note that each VM has its own guest OS, bins, libraries and application, usually all deployed bespoke by-hand (think deploying MS SQL, installing .Net as a prerequisite, etc) even if not deployed by hand they can be deployed with a framework like vRA, Ansible, Puppet, Chef, et al.

This is not the case for the containers on the right hand side of the diagram. The app code, bins and libraries are all self-contained (heh), but the guest-os is shared between them. The separation and security boundary moves up the stack from the VM level to the OS-process level.

## Why do I need them

What's the problem with doing things the "VM way" above I hear you ask? Easy - if (when) something changes inside the VM; a library is updated, application is updated, and it has unexpected effects on the way the application runs how easy is that to troubleshoot or roll back? How easy is it to know _something_ has changed without trawling logs?

The answer, quite simply, is that it's not. There is no "known good state" inside a VM, they are ever-changing and evolving over their life cycle and as such get a reputation of being "pets" with special temperaments and needs usually kept as tribal knowledge by the operations team.

Managing a VM goes like this; install a guest operating system, patch it, install the app prerequisites, then install the app and manage its life cycle, updating each component in turn, in the correct order and dealing with strange artifacts left behind as a result of upgrades from one version to another that are left on the guest os.

### How do containers help me solve these operational problems

Containers allow applications to be packaged as an immutable unit, deployed consistently, always in a known-good state. Then, when upgrade time comes - the container is destroyed and another is spun up in its place inheriting the state of the old container (more on this and volume mappings later).

The other nice thing is that containers are usually built and published in combination with `git` and tags or some sort of versioning tool, meaning that when a new version is spun up - we know because the container's metadata will have changed and we can simply roll back to the previous version!

That's not all of the benefits, but even at that it solves a lot of problems, if you ask me.

## It wouldn't be an intro without Docker

Containers and Docker are largely synonyms to the uninitiated, however they are different and there is a lot more to the container ecosystem than just Docker. To start with Docker, Inc. is the company that was spun out from the open source Docker project that originally defined the container "image" and "runtime" standards which are now managed as part of the Open Container Initiative (OCI) in order to prevent ecosystem fragmentation and lock-in.

I'll break down Docker's components into a few parts:

* Engine
* Image
* Runtime
* Command Line

### The Docker Engine (dockerd)

The Docker Engine also known by it's daemon name `dockerd` is the process that provides the "Docker" wrapper around the lower level components in the container stack, that make it easy to interface with, an API and a CLI.

### The Image

A container image (also known as an OCI image) is the distribution unit of a container - as mentioned back at the start, essentially a tarball with all the "stuff" in it that makes the app run. These can be arbitrarily tagged to distribute different versions of the application that can be run side-by-side with other containers instantiated from that image, or can be used to replace previous versions of the container instance.

### The Runtime (containerd)

A container runtime is the process that actually executes the processes within the container instance that is deployed.

### The CLI

All communications from the docker command-line tool `docker` are done via [the Docker Engine API](https://docs.docker.com/engine/api/v1.39/). The engine either binds to a local unix socket: `unix:///var/run/docker.sock` (for local machine use) or an IP address and port, in order to act as a remote host for access by other machines. The Docker Engine API is RESTful and can actually be used without the CLI, but the CLI is much more human-friendly than raw JSON.

## Next time on the CNA Ninja Series

The above introduced the components of containers, where they came from, what Docker is and why you should care about containers from an operational point of view. Now that you know the history and the core concepts - how about getting stuck in and building a container? Check out [Part 2 - Your First Container](../02_First-Container/) where we create and docker container from scratch and deploy it!

Stay tuned for updates to the CNA Ninja series, give [the repository](https://github.com/mylesagray/cna-ninja) a "Watch" to be alerted of the next release!