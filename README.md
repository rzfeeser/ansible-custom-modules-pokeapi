# rzfeeser.pokeapi - PokeAPI.co Ansible Collection
Author: Russell Zachary Feeser  
GitHub: @RZFeeser  
 Email: rzfeeser@users.noreply.github.com  
Galaxy: https://galaxy.ansible.com/rzfeeser/pokeapi  

![rzfeeser.pokeapi Pokemon Banner](https://github.com/rzfeeser/ansible-custom-modules-pokeapi/blob/main/docs/images/pokeapi_graphic.png?raw=true)

This repository is an ansible collection, `rzfeeser.pokeapi`, written by @RZFeeser for the purposes of an Ansible collection containing plugins and playbooks that abstract interaction with API v2 service @ [pokeapi.co](https://pokeapi.co/)


### Resources
- [@GitHub - rzfeeser/ansible-custom-modules-pokeapi](https://github.com/rzfeeser/ansible-custom-modules-pokeapi)
- [@GitLab - PokeAPI Ansible Execution Environment](https://gitlab.com/rzfeeser/ansible-execution-environments)
- [pokeapi.co](https://pokeapi.co/)
- [Ansible Galaxy - rzfeeser.pokeapi](https://galaxy.ansible.com/rzfeeser/pokeapi)


### Install Notes
- This Ansible collection is written with the Python standard library, so it has no dependenies beyond itself.
- This is an Ansible collection and may be installed using one of the following methods:
  1. Install directly from source on GitHub
  2. Proxied from ansible.galaxy.com
  3. Bypass a direct install, and instead use the PokeAPI Execution Environment container based solution (suitable for CI engines such as AAP/Tower/AWX, Jenkins, GitLab, and so on)

#### Option 01 - Install directly from source on Github
- Ansible should already be installed
- Install rzfeeser.pokeapi collection directly from GitHub - `ansible-galaxy collection install git+https://github.com/rzfeeser/ansible-custom-modules-pokeapi`

#### Option 02 - Proxied from ansible.galaxy.com
- Ansible should already be installed
- Install rzfeeser.pokeapi collection via ansible.galaxy.com - `ansible-galaxy collection install rzfeeser.pokeapi`

#### Option 03 - Container based solution
- `ansible-runner` needs to be installed, and Docker needs to exist
  - It should be mentioned that `ansible-runner` requires a special project directory layout before executing. See the [ansible-runner Project Homepage](https://ansible.readthedocs.io/projects/runner/en/stable/index.html) for more information
- An Ansible Execution Environment container is maintained by this author, [@RZFeeser on GitLab](https://gitlab.com/rzfeeser/ansible-execution-environments). This solution includes Ansible, Python, Ansible-Runner, and the most recent `rzfeeser.pokeapi` collection
- Use `ansible-runner` to run a playbook containing references to the `rzfeeser.pokeapi` collection - `ansible-runner run --process-isolation --process-isolation-executable docker --container-image registry.gitlab.com/rzfeeser/ansible-execution-environments/pokeapi-ee -p playbook_to_run.yml .`


### How to Use
- The module `rzfeeser.pokeapi.pokeapi_info` may be used to make API requests to pokeapi.co/api/v2/. This module was written to simplify interaction with pokeapi.co/v2 API. See pokeapi.co for documentation on using the v2 API. It has the following options:


- `rzfeeser.pokeapi.pokeapi_info` has the following options:
  - **resource**:
      description: This is the resource to lookup. See pokeapi.co/docs/v2 for all possible values. Values include 'ability', 'berry', 'berry-firmness', 'berry-flavor', 'characteristic', 'contest-effect', 'contest-type', 'egg-group', 'encounter-condition', 'encounter-condition-value', 'encounter-method', 'evolution-chain', 'evolution-trigger', 'gender', 'generation', 'growth-rate', 'item', 'item-attribute', 'item-category', 'item-fling-effect', 'item-pocket', 'language', 'location', 'location-area', 'machine', 'move', 'move-ailment', 'move-battle-style', 'move-category', 'move-damage-class', 'move-learn-method', 'move-target', 'nature', 'pal-park-area', 'pokeathlon-stat', 'pokedex', 'pokemon', 'pokemon-color', 'pokemon-form', 'pokemon-habitat', 'pokemon-shape', 'pokemon-species', 'region', 'stat', 'super-contest-effect', 'type', 'version', 'version-group'
      required: true
      type: str
  - **name**:
      description: The name of the resource to lookup. See pokeapi.co/docs/v2 for all possible values.
      required: false
      type: str
  - **limit**:
      description: The number of results that will be returned with the lookup.
      required: false
      type: int
  - **offset**:
      description: The resource index + 1 to begin at. For example, If 42 is passed, then resource 43 will be the first result returned.
      required: false
      type: int


### About PokeAPI.co REST API
Visit [PokeAPI.co](https://pokeapi.co/) for more information about the project.

### About the Author
Russell Zachary Feeser (@RZFeeser) is a consultant and technology trainer focusing on Ansible, Python, AWX/Tower/AAP, Terraform, Go, Azure, 5G and core telecom communications. If you're interested in discussing a consulting or training project, feel free to reach out.
