Cool, so now we've persisted the storage within the container to the guest os that the container runs on, however another fundamental pillar of containers is easy scalability, generally across nodes - it would be cumbersome and non-sensicle to do this manually, so there must be a better way to scale containerised applications.

This means that your new deployment goes from the above to `docker run redis` and you'll have an up and running redis instance. Granted, this is a very simple example, most `docker run` commands require some more input parameters, but the premise is the same.

## The need for an orchestrator

I mentioned Kubernetes at the start, and this is where it fits in.

## The container ecosystem

As you may have noticed in the past few years we have been ramping up our efforts on investing in and releasing container-centric products, further expanded upon recently through our acquisition of [Heptio](https://heptio.com).

Over the past few years we began exploring the container ecosystem and how we can better integrate and lead in this space – the genesis of this was [VMware Integrated Containers (VIC)](https://www.vmware.com/uk/products/vsphere/integrated-containers.html), VIC allowed developers to deploy arbitrary containers to a Docker compatible API endpoint (VIC) and at the same time, it allowed the vSphere admin visibility into the containers that were running inside these VIC VMs by exposing them as first-class citizens in vSphere.

![VIC](../../11/CNA-Ninja-Pt-1/VIC.png)

_figure 3 shows how VIC places containers alongside VMs as first class citizens in vSphere_

Further to that we released, in partnership with Pivotal, [Pivotal Container Services (PKS)](https://pivotal.io/platform/pivotal-container-service) -  the `K` here stands for Kubernetes, PKS provides developers the ability to self-service deploy K8S clusters as well as scale them on demand. Kubernetes being the defacto standard for container orchestrators in use today - more on this later.