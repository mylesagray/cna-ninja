# CNA Ninja Series

## Taking an app on a journey

Through this whole learning series - we’ll start with some code that runs on your laptop natively, built in python - illustrating the challenges with different library versions and code shipping to production. We'll containerise it and run it locally, showing how that solves some of the problems we encountered. Following that we are going to abstract the data and app planes for a more microservice-style approach, show volume persistence in the data plane container and why it's important, additionally demo connectivity between containers using nothing but the built-in dns inherent within the platform. Then continue to evolve the app with each step until it’s fully fault tolerant, K8s native, using all the bells and whistles, CI/CD automated rollouts, canary releases via service mesh with Isito and more.

## The Parts

1. [Why Containers, why now?](01_Why-Containers/)