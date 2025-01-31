# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Create(AAZCommand):
    """Creates an Endpoint resource, which represents a data transfer source or destination.
    """

    _aaz_info = {
        "version": "2023-07-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.storagemover/storagemovers/{}/endpoints/{}", "2023-07-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.endpoint_name = AAZStrArg(
            options=["-n", "--name", "--endpoint-name"],
            help="The name of the Endpoint resource.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.storage_mover_name = AAZStrArg(
            options=["--storage-mover-name"],
            help="The name of the Storage Mover resource.",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.storage_blob_container = AAZObjectArg(
            options=["--storage-blob-container"],
            arg_group="Properties",
            help="Storage Blob Container Object",
        )
        _args_schema.azure_storage_smb_file_share = AAZObjectArg(
            options=["--azure-storage-smb-file-share"],
            arg_group="Properties",
        )
        _args_schema.nfs_mount = AAZObjectArg(
            options=["--nfs-mount"],
            arg_group="Properties",
        )
        _args_schema.smb_mount = AAZObjectArg(
            options=["--smb-mount"],
            arg_group="Properties",
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="A description for the Endpoint.",
        )

        storage_blob_container = cls._args_schema.storage_blob_container
        storage_blob_container.blob_container_name = AAZStrArg(
            options=["blob-container-name"],
            help="The name of the Storage blob container that is the target destination.",
            required=True,
        )
        storage_blob_container.storage_account_resource_id = AAZResourceIdArg(
            options=["storage-account-resource-id"],
            help="The Azure Resource ID of the storage account that is the target destination.",
            required=True,
        )

        azure_storage_smb_file_share = cls._args_schema.azure_storage_smb_file_share
        azure_storage_smb_file_share.file_share_name = AAZStrArg(
            options=["file-share-name"],
            help="The name of the Azure Storage file share.",
            required=True,
        )
        azure_storage_smb_file_share.storage_account_resource_id = AAZResourceIdArg(
            options=["storage-account-resource-id"],
            help="The Azure Resource ID of the storage account.",
            required=True,
        )

        nfs_mount = cls._args_schema.nfs_mount
        nfs_mount.export = AAZStrArg(
            options=["export"],
            help="The directory being exported from the server.",
            required=True,
        )
        nfs_mount.host = AAZStrArg(
            options=["host"],
            help="The host name or IP address of the server exporting the file system.",
            required=True,
        )
        nfs_mount.nfs_version = AAZStrArg(
            options=["nfs-version"],
            help="The NFS protocol version.",
            enum={"NFSauto": "NFSauto", "NFSv3": "NFSv3", "NFSv4": "NFSv4"},
        )

        smb_mount = cls._args_schema.smb_mount
        smb_mount.credentials = AAZObjectArg(
            options=["credentials"],
            help="The Azure Key Vault secret URIs which store the required credentials to access the SMB share.",
        )
        smb_mount.host = AAZStrArg(
            options=["host"],
            help="The host name or IP address of the server exporting the file system.",
            required=True,
        )
        smb_mount.share_name = AAZStrArg(
            options=["share-name"],
            help="The name of the SMB share being exported from the server.",
            required=True,
        )

        credentials = cls._args_schema.smb_mount.credentials
        credentials.password_uri = AAZStrArg(
            options=["password-uri"],
            help="The Azure Key Vault secret URI which stores the password. Use empty string to clean-up existing value.",
        )
        credentials.username_uri = AAZStrArg(
            options=["username-uri"],
            help="The Azure Key Vault secret URI which stores the username. Use empty string to clean-up existing value.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.EndpointsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class EndpointsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageMover/storageMovers/{storageMoverName}/endpoints/{endpointName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "endpointName", self.ctx.args.endpoint_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "storageMoverName", self.ctx.args.storage_mover_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-07-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_const("endpointType", "AzureStorageBlobContainer", AAZStrType, ".storage_blob_container", typ_kwargs={"flags": {"required": True}})
                properties.set_const("endpointType", "AzureStorageSmbFileShare", AAZStrType, ".azure_storage_smb_file_share", typ_kwargs={"flags": {"required": True}})
                properties.set_const("endpointType", "NfsMount", AAZStrType, ".nfs_mount", typ_kwargs={"flags": {"required": True}})
                properties.set_const("endpointType", "SmbMount", AAZStrType, ".smb_mount", typ_kwargs={"flags": {"required": True}})
                properties.discriminate_by("endpointType", "AzureStorageBlobContainer")
                properties.discriminate_by("endpointType", "AzureStorageSmbFileShare")
                properties.discriminate_by("endpointType", "NfsMount")
                properties.discriminate_by("endpointType", "SmbMount")

            disc_azure_storage_blob_container = _builder.get(".properties{endpointType:AzureStorageBlobContainer}")
            if disc_azure_storage_blob_container is not None:
                disc_azure_storage_blob_container.set_prop("blobContainerName", AAZStrType, ".storage_blob_container.blob_container_name", typ_kwargs={"flags": {"required": True}})
                disc_azure_storage_blob_container.set_prop("storageAccountResourceId", AAZStrType, ".storage_blob_container.storage_account_resource_id", typ_kwargs={"flags": {"required": True}})

            disc_azure_storage_smb_file_share = _builder.get(".properties{endpointType:AzureStorageSmbFileShare}")
            if disc_azure_storage_smb_file_share is not None:
                disc_azure_storage_smb_file_share.set_prop("fileShareName", AAZStrType, ".azure_storage_smb_file_share.file_share_name", typ_kwargs={"flags": {"required": True}})
                disc_azure_storage_smb_file_share.set_prop("storageAccountResourceId", AAZStrType, ".azure_storage_smb_file_share.storage_account_resource_id", typ_kwargs={"flags": {"required": True}})

            disc_nfs_mount = _builder.get(".properties{endpointType:NfsMount}")
            if disc_nfs_mount is not None:
                disc_nfs_mount.set_prop("export", AAZStrType, ".nfs_mount.export", typ_kwargs={"flags": {"required": True}})
                disc_nfs_mount.set_prop("host", AAZStrType, ".nfs_mount.host", typ_kwargs={"flags": {"required": True}})
                disc_nfs_mount.set_prop("nfsVersion", AAZStrType, ".nfs_mount.nfs_version")

            disc_smb_mount = _builder.get(".properties{endpointType:SmbMount}")
            if disc_smb_mount is not None:
                disc_smb_mount.set_prop("credentials", AAZObjectType, ".smb_mount.credentials")
                disc_smb_mount.set_prop("host", AAZStrType, ".smb_mount.host", typ_kwargs={"flags": {"required": True}})
                disc_smb_mount.set_prop("shareName", AAZStrType, ".smb_mount.share_name", typ_kwargs={"flags": {"required": True}})

            credentials = _builder.get(".properties{endpointType:SmbMount}.credentials")
            if credentials is not None:
                credentials.set_prop("passwordUri", AAZStrType, ".password_uri")
                credentials.set_const("type", "AzureKeyVaultSmb", AAZStrType, ".", typ_kwargs={"flags": {"required": True}})
                credentials.set_prop("usernameUri", AAZStrType, ".username_uri")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.description = AAZStrType()
            properties.endpoint_type = AAZStrType(
                serialized_name="endpointType",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            disc_azure_storage_blob_container = cls._schema_on_200.properties.discriminate_by("endpoint_type", "AzureStorageBlobContainer")
            disc_azure_storage_blob_container.blob_container_name = AAZStrType(
                serialized_name="blobContainerName",
                flags={"required": True},
            )
            disc_azure_storage_blob_container.storage_account_resource_id = AAZStrType(
                serialized_name="storageAccountResourceId",
                flags={"required": True},
            )

            disc_azure_storage_smb_file_share = cls._schema_on_200.properties.discriminate_by("endpoint_type", "AzureStorageSmbFileShare")
            disc_azure_storage_smb_file_share.file_share_name = AAZStrType(
                serialized_name="fileShareName",
                flags={"required": True},
            )
            disc_azure_storage_smb_file_share.storage_account_resource_id = AAZStrType(
                serialized_name="storageAccountResourceId",
                flags={"required": True},
            )

            disc_nfs_mount = cls._schema_on_200.properties.discriminate_by("endpoint_type", "NfsMount")
            disc_nfs_mount.export = AAZStrType(
                flags={"required": True},
            )
            disc_nfs_mount.host = AAZStrType(
                flags={"required": True},
            )
            disc_nfs_mount.nfs_version = AAZStrType(
                serialized_name="nfsVersion",
            )

            disc_smb_mount = cls._schema_on_200.properties.discriminate_by("endpoint_type", "SmbMount")
            disc_smb_mount.credentials = AAZObjectType()
            disc_smb_mount.host = AAZStrType(
                flags={"required": True},
            )
            disc_smb_mount.share_name = AAZStrType(
                serialized_name="shareName",
                flags={"required": True},
            )

            credentials = cls._schema_on_200.properties.discriminate_by("endpoint_type", "SmbMount").credentials
            credentials.password_uri = AAZStrType(
                serialized_name="passwordUri",
            )
            credentials.type = AAZStrType(
                flags={"required": True},
            )
            credentials.username_uri = AAZStrType(
                serialized_name="usernameUri",
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
