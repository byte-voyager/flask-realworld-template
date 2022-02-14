from flask import Blueprint


class V1BluePoint(Blueprint):
    URL_PREFIX_VERSION = "/api/v1"

    def __init__(
        self,
        name,
        import_name=__name__,
        static_folder=None,
        static_url_path=None,
        template_folder=None,
        url_prefix=None,
        subdomain=None,
        url_defaults=None,
        root_path=None,
    ):
        super(V1BluePoint, self).__init__(
            name=name,
            import_name=import_name,
            static_folder=static_folder,
            static_url_path=static_url_path,
            template_folder=template_folder,
            url_prefix=self.URL_PREFIX_VERSION + url_prefix,
            subdomain=subdomain,
            url_defaults=url_defaults,
            root_path=root_path,
        )
