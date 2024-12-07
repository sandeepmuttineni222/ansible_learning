# Learning Ansible

This repository contains resources and notes to help you learn **Ansible**, an open-source automation tool used for configuration management, application deployment, and task automation.

---

## Table of Contents

1. [Introduction to Ansible](#introduction-to-ansible)
2. [Prerequisites](#prerequisites)
3. [Setting Up Ansible](#setting-up-ansible)
4. [Basic Ansible Concepts](#basic-ansible-concepts)
5. [Writing Your First Playbook](#writing-your-first-playbook)
6. [Ansible Commands](#ansible-commands)
7. [Ansible Roles and Collections](#ansible-roles-and-collections)
8. [Useful Resources](#useful-resources)

---

## Introduction to Ansible

Ansible is a simple, agentless, and powerful automation tool. It uses **SSH** to communicate with remote servers and execute tasks, making it an ideal choice for managing large numbers of systems. It is used for:

- **Configuration management**
- **Application deployment**
- **Automating repetitive tasks**

Key features:
- Simple YAML syntax (Human-readable)
- Agentless architecture
- Idempotent (safe to run multiple times)

---

## Prerequisites

Before you begin using Ansible, ensure you have the following:

- A basic understanding of Linux/Unix commands
- Access to a machine where you can install Ansible
- SSH access to remote machines (for Ansible to manage them)

---

## Setting Up Ansible

### 1. Install Ansible

You can install Ansible on most Linux distributions. Here’s an example for **Ubuntu**:

```bash
sudo apt update
sudo apt install ansible
