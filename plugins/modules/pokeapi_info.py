#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pokeapi_info

short_description: Make lookups to pokeapi.co/v2

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This module was written to simplify interaction with pokeapi.co/v2 API. See pokeapi.co for documentation on using the v2 API.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Russell Zachary Feeser (@rzfeeser)
'''

EXAMPLES = r'''
# return JSON to pokeapi.co/v2/pokemon/pikachu
- name: make a call to pokeapi
  pokeapi_info:
    resource: pokemon      # (group) describes the resource or group within the pokeapi.co service the user wants
    name: pikachu          # (id) describes the name or id within the resource to search on
  register: results

- name: display pokemon/pikachu results
  ansible.builtin.debug:
    var: results

# return JSON to pokeapi.co/v2/pokemon?limit=100&offset=42
- name: make a call to pokeapi with limit of 10 and offset of 100
  pokeapi_info:
    resource: pokemon
    limit: 100      # stop at 142 (limit to 100 results)
    offset: 42      # start at 43
  register: results

- name: display pokemon?limit=100&offset=42 results
  ansible.builtin.debug:
    var: results

# return JSON to pokeapi.co/v2/berry
- name: make a call to the resource berry
  pokeapi_info:
    resource: berry
  register: results

- name: display display berry results
  ansible.builtin.debug:
    var: results
'''

RETURN = r'''
pokeapi_json:
    description: The JSON returned by the lookup to pokeapi.co/v2
    type: dict
    returned: always
    sample: {"count":64,"next":"https://pokeapi.co/api/v2/berry?offset=1&limit=1","previous":null,"results":[{"name":"cheri","url":"https://pokeapi.co/api/v2/berry/1/"}]}

status_code:
    description: The HTTP status code returned by the lookup to pokeapi.co/v2
    type: str   # confirm this
    returned: always
    sample: '200'

name:
    description: The name that was passed into the module
    type: str | None
    returned: always
    sample: "pikachu"

resource: 
    description: The resource that was passed into the module
    type: str
    returned: always
    sample: pokemon

limit:
    description: The limit that was passed into the module
    type: int
    returned: always
    sample: 42

offset:
    description: The offset that was passed into the module
    type: int
    returned: always
    sample: 100
'''

# standard library
import urllib.request
import json

# python3 -m pip install ansible
from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=False),
        resource=dict(type='str', required=True),
        limit=dict(type='int', required=False),
        offset=dict(type='int', required=False)
    )


    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )


    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        pokeapi_json='',
        status_code='',
        name=module.params.get('name'),
        resource=module.params.get('resource'),
        limit=module.params.get('limit'),
        offset=module.params.get('offset')
    )




    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)



    poke_url = f"https://pokeapi.co/api/v2/{ module.params['resource'] }"

    if module.params['name']:
        poke_url = f"{ poke_url }/{ module.params['name'] }?"
    else:
        poke_url = f"{ poke_url }?"

    # did they include a limit parameter
    if module.params['limit']:
        poke_url = f"{poke_url}limit={module.params['limit']}&"
    if module.params['offset']:
        poke_url = f"{poke_url}offset={module.params['offset']}&"

   
    # prepare to call the api
    # we must include a header to make our script appear as if the request is coming from a browser
    req = urllib.request.Request(
        url=poke_url,
        headers={"User-Agent": "Mozilla/5.0"}
        )

    # call the API
    pokeresp = urllib.request.urlopen(req)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a bytes-like string
    # therefore we translate it to UTF-8
    pokemon_info = pokeresp.read()
    pokemon_info = json.loads(pokemon_info.decode("utf-8"))


    # assign data to our results (returned JSON)
    result['pokeapi_json'] = pokemon_info
    result['status_code'] = pokeresp.code

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
