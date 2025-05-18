# Cloud-Management-System
Cloud Management System is a Python-based GUI application designed to simplify virtualization and containerization management. It allows users to create and manage Virtual Machines (VMs) using QEMU and control Docker containers and images through an intuitive Tkinter interface.

Features
Create Virtual Machines with custom CPU, memory, disk size, and ISO image.

Generate Dockerfiles dynamically via GUI.

Build Docker images from custom Dockerfiles.

List Docker images and running containers.

Stop running Docker containers easily.

Search for Docker images locally and on DockerHub.

Pull Docker images directly from DockerHub.

Technologies Used
Python 3.11 — Main programming language

Tkinter — GUI framework for user interface

QEMU — Virtual machine management

Docker — Containerization platform

OS module — System command execution

Installation
Prerequisites
Python 3 installed ([Download Python](https://www.python.org/downloads/))

Docker installed and running ([Get Docker](https://docs.docker.com/get-docker/))

QEMU installed (https://www.qemu.org/download/)

Workflow
Click Create Virtual Machine to set CPU, memory, disk size, and select an ISO file to start a VM.

Use Create Dockerfile to write and save Dockerfiles.

Build images via Build Docker Image by specifying Dockerfile path and image name.

List images or running containers via respective buttons.

Stop containers by specifying container ID or name.

Search images locally or on DockerHub.

Pull images from DockerHub by specifying image name/tag.
