# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: huangrh@goodrain.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.v1_store_app_version_templete import V1StoreAppVersionTemplete  # noqa: E501
from openapi_client.rest import ApiException

class TestV1StoreAppVersionTemplete(unittest.TestCase):
    """V1StoreAppVersionTemplete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1StoreAppVersionTemplete
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1_store_app_version_templete.V1StoreAppVersionTemplete()  # noqa: E501
        if include_optional :
            return V1StoreAppVersionTemplete(
                apps = [
                    openapi_client.models.v1/store_app_version_templete_app.v1.StoreAppVersionTempleteApp(
                        category = '0', 
                        cmd = '0', 
                        dep_service_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_dep_service.v1.StoreAppVersionTempleteAppDepService(
                                dep_service_key = '0', )
                            ], 
                        deploy_version = '0', 
                        extend_method = '0', 
                        extend_method_map = openapi_client.models.v1/store_app_version_templete_app_extend_method_rule.v1.StoreAppVersionTempleteAppExtendMethodRule(
                            is_restart = 56, 
                            max_memory = 56, 
                            max_node = 56, 
                            min_memory = 56, 
                            min_node = 56, 
                            step_memory = 56, 
                            step_node = 56, ), 
                        image = '0', 
                        language = '0', 
                        memory = 56, 
                        mnt_relation_list = [
                            openapi_client.models.v1/store_app_version_templete_app_share_volume.v1.StoreAppVersionTempleteAppShareVolume(
                                mnt_dir = '0', 
                                mnt_name = '0', 
                                service_share_uuid = '0', )
                            ], 
                        port_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_port.v1.StoreAppVersionTempleteAppPort(
                                container_port = 56, 
                                is_inner_service = True, 
                                is_outer_service = True, 
                                port_alias = '0', 
                                protocol = '0', 
                                tenant_id = '0', )
                            ], 
                        probes = [
                            openapi_client.models.v1/store_app_version_templete_app_probe.v1.StoreAppVersionTempleteAppProbe(
                                id = 56, 
                                cmd = '0', 
                                failure_threshold = 56, 
                                http_header = '0', 
                                initial_delay_second = 56, 
                                is_used = True, 
                                mode = '0', 
                                path = '0', 
                                period_second = 56, 
                                port = 56, 
                                probe_id = '0', 
                                scheme = '0', 
                                service_id = '0', 
                                success_threshold = 56, 
                                timeout_second = 56, )
                            ], 
                        service_alias = '0', 
                        service_cname = '0', 
                        service_connect_info_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_env.v1.StoreAppVersionTempleteAppEnv(
                                attr_name = '0', 
                                attr_value = '0', 
                                is_change = True, 
                                name = '0', )
                            ], 
                        service_env_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_env.v1.StoreAppVersionTempleteAppEnv(
                                attr_name = '0', 
                                attr_value = '0', 
                                is_change = True, 
                                name = '0', )
                            ], 
                        service_id = '0', 
                        service_image = openapi_client.models.v1/image_info.v1.ImageInfo(
                            hub_password = '0', 
                            hub_url = '0', 
                            hub_user = '0', 
                            is_trust = True, 
                            namespace = '0', ), 
                        service_key = '0', 
                        service_name = '0', 
                        service_region = '0', 
                        service_related_plugin_config = [
                            openapi_client.models.v1/store_app_version_templete_app_plugin_config.v1.StoreAppVersionTempleteAppPluginConfig(
                                id = 56, 
                                attr = [
                                    openapi_client.models.v1/store_app_version_templete_app_plugin_config/attr.v1.StoreAppVersionTempleteAppPluginConfig.attr()
                                    ], 
                                build_version = '0', 
                                create_time = '0', 
                                plugin_id = '0', 
                                plugin_key = '0', 
                                plugin_status = True, 
                                service_id = '0', 
                                service_meta_type = '0', )
                            ], 
                        service_share_uuid = '0', 
                        service_source = '0', 
                        service_type = '0', 
                        service_volume_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_volume.v1.StoreAppVersionTempleteAppVolume(
                                access_mode = '0', 
                                file_content = '0', 
                                volume_capacity = 56, 
                                volume_name = '0', 
                                volume_path = '0', 
                                volume_type = '0', )
                            ], 
                        share_image = '0', 
                        share_type = '0', 
                        tenant_id = '0', 
                        version = '0', )
                    ], 
                group_key = '0', 
                group_name = '0', 
                group_version = '0', 
                plugins = [
                    openapi_client.models.v1/store_app_version_templete_plugin.v1.StoreAppVersionTempletePlugin(
                        id = 56, 
                        build_source = '0', 
                        build_version = '0', 
                        category = '0', 
                        code_repo = '0', 
                        config_groups = [
                            openapi_client.models.v1/store_app_version_templete_plugin_config_group.v1.StoreAppVersionTempletePluginConfigGroup(
                                id = 56, 
                                build_version = '0', 
                                config_name = '0', 
                                injection = '0', 
                                options = [
                                    openapi_client.models.v1/store_app_version_templete_plugin_config_group_option.v1.StoreAppVersionTempletePluginConfigGroupOption(
                                        id = 56, 
                                        attr_alt_value = '0', 
                                        attr_default_value = '0', 
                                        attr_info = '0', 
                                        attr_name = '0', 
                                        attr_type = '0', 
                                        build_version = '0', 
                                        is_change = True, 
                                        plugin_id = '0', 
                                        protocol = '0', 
                                        service_meta_type = '0', )
                                    ], 
                                plugin_id = '0', 
                                service_meta_type = '0', )
                            ], 
                        create_time = '0', 
                        desc = '0', 
                        image = '0', 
                        origin = '0', 
                        origin_share_id = '0', 
                        plugin_alias = '0', 
                        plugin_id = '0', 
                        plugin_image = openapi_client.models.v1/image_info.v1.ImageInfo(
                            hub_password = '0', 
                            hub_url = '0', 
                            hub_user = '0', 
                            is_trust = True, 
                            namespace = '0', ), 
                        plugin_key = '0', 
                        plugin_name = '0', 
                        share_image = '0', )
                    ], 
                template_version = '0'
            )
        else :
            return V1StoreAppVersionTemplete(
                apps = [
                    openapi_client.models.v1/store_app_version_templete_app.v1.StoreAppVersionTempleteApp(
                        category = '0', 
                        cmd = '0', 
                        dep_service_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_dep_service.v1.StoreAppVersionTempleteAppDepService(
                                dep_service_key = '0', )
                            ], 
                        deploy_version = '0', 
                        extend_method = '0', 
                        extend_method_map = openapi_client.models.v1/store_app_version_templete_app_extend_method_rule.v1.StoreAppVersionTempleteAppExtendMethodRule(
                            is_restart = 56, 
                            max_memory = 56, 
                            max_node = 56, 
                            min_memory = 56, 
                            min_node = 56, 
                            step_memory = 56, 
                            step_node = 56, ), 
                        image = '0', 
                        language = '0', 
                        memory = 56, 
                        mnt_relation_list = [
                            openapi_client.models.v1/store_app_version_templete_app_share_volume.v1.StoreAppVersionTempleteAppShareVolume(
                                mnt_dir = '0', 
                                mnt_name = '0', 
                                service_share_uuid = '0', )
                            ], 
                        port_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_port.v1.StoreAppVersionTempleteAppPort(
                                container_port = 56, 
                                is_inner_service = True, 
                                is_outer_service = True, 
                                port_alias = '0', 
                                protocol = '0', 
                                tenant_id = '0', )
                            ], 
                        probes = [
                            openapi_client.models.v1/store_app_version_templete_app_probe.v1.StoreAppVersionTempleteAppProbe(
                                id = 56, 
                                cmd = '0', 
                                failure_threshold = 56, 
                                http_header = '0', 
                                initial_delay_second = 56, 
                                is_used = True, 
                                mode = '0', 
                                path = '0', 
                                period_second = 56, 
                                port = 56, 
                                probe_id = '0', 
                                scheme = '0', 
                                service_id = '0', 
                                success_threshold = 56, 
                                timeout_second = 56, )
                            ], 
                        service_alias = '0', 
                        service_cname = '0', 
                        service_connect_info_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_env.v1.StoreAppVersionTempleteAppEnv(
                                attr_name = '0', 
                                attr_value = '0', 
                                is_change = True, 
                                name = '0', )
                            ], 
                        service_env_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_env.v1.StoreAppVersionTempleteAppEnv(
                                attr_name = '0', 
                                attr_value = '0', 
                                is_change = True, 
                                name = '0', )
                            ], 
                        service_id = '0', 
                        service_image = openapi_client.models.v1/image_info.v1.ImageInfo(
                            hub_password = '0', 
                            hub_url = '0', 
                            hub_user = '0', 
                            is_trust = True, 
                            namespace = '0', ), 
                        service_key = '0', 
                        service_name = '0', 
                        service_region = '0', 
                        service_related_plugin_config = [
                            openapi_client.models.v1/store_app_version_templete_app_plugin_config.v1.StoreAppVersionTempleteAppPluginConfig(
                                id = 56, 
                                attr = [
                                    openapi_client.models.v1/store_app_version_templete_app_plugin_config/attr.v1.StoreAppVersionTempleteAppPluginConfig.attr()
                                    ], 
                                build_version = '0', 
                                create_time = '0', 
                                plugin_id = '0', 
                                plugin_key = '0', 
                                plugin_status = True, 
                                service_id = '0', 
                                service_meta_type = '0', )
                            ], 
                        service_share_uuid = '0', 
                        service_source = '0', 
                        service_type = '0', 
                        service_volume_map_list = [
                            openapi_client.models.v1/store_app_version_templete_app_volume.v1.StoreAppVersionTempleteAppVolume(
                                access_mode = '0', 
                                file_content = '0', 
                                volume_capacity = 56, 
                                volume_name = '0', 
                                volume_path = '0', 
                                volume_type = '0', )
                            ], 
                        share_image = '0', 
                        share_type = '0', 
                        tenant_id = '0', 
                        version = '0', )
                    ],
                group_key = '0',
                group_name = '0',
                group_version = '0',
                template_version = '0',
        )

    def testV1StoreAppVersionTemplete(self):
        """Test V1StoreAppVersionTemplete"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()