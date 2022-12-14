# -*- coding: utf-8 -*-
"""
Copyright 2019 eBay Inc.
 
Licensed under the Apache License, Version 2.0 (the "License");
You may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,

WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and
limitations under the License.
"""
import json
import logging
from model.model import environment, credentials

user_config_ids = ["sandbox-user", "production-user"]

class credentialutil(object):
    """
    credential_list: dictionary key=string, value=credentials
    """
    _credential_list = {}
    
     
    @classmethod
    def load(cls, app_config_path):

        logging.info("Loading credential configuration file at: %s", app_config_path)
        with open(app_config_path, 'r') as f:
            if app_config_path.endswith('.json'):
                content = json.loads(f.read())
                """
                _________________________
                app_config_path: {app_config_path}
                _________________________
                load content: {content}
                """
            else:
                raise ValueError('Configuration file need to be in JSON')
            credentialutil._iterate(content)

    @classmethod
    def _iterate(cls, content):
        """
        _________________________
        _iterate content: {content}
        """
        for key in content:
            logging.debug("Environment attempted: %s", key)

            if key in [environment.PRODUCTION.config_id, environment.SANDBOX.config_id]:     
                client_id = content[key]['appid']
                dev_id = content[key]['devid']
                client_secret = content[key]['certid']
                ru_name = content[key]['redirecturi']

                app_info = credentials(client_id, client_secret, dev_id, ru_name)
                cls._credential_list.update({key: app_info})
                """
                _________________________
                key: {key}
                _________________________
                client_id: {client_id}
                _________________________
                dev_id: {dev_id}
                _________________________
                client_secret: {client_secret}
                _________________________
                ru_name: {ru_name}
                _________________________
                app_info: {app_info}
                _________________________
                _iterate cls._credential_list: {str(cls._credential_list)}
                """

            

    @classmethod
    def get_credentials(cls, env_type):
        """
        env_config_id: environment.PRODUCTION.config_id or environment.SANDBOX.config_id
        """
        """
        _________________________
        get_credentials cls._credential_list: {cls._credential_list}
        _________________________
        get_credentials env_type: {env_type.config_id}
        _________________________
        get_credentials cls._credential_list[env_type.config_id]:
        _________________________
        """

        if len(cls._credential_list) == 0:
            msg = "No environment loaded from configuration file"
            logging.error(msg)
            raise CredentialNotLoadedError(msg)
        return cls._credential_list[env_type.config_id]
    
class CredentialNotLoadedError(Exception):
    pass