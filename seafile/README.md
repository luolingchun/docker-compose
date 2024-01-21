
docker cp sea-onlyoffice:/etc/onlyoffice/documentserver/default.json ./

修改以下值为：

```json
...
"request-filtering-agent" : {
				"allowPrivateIPAddress": true,
				"allowMetaIPAddress": true
			},
...
```

在docker-compose中添加挂载：

- ./default.json:/etc/onlyoffice/documentserver/default.json


编辑./data/seafile-data/seafile/conf/seahub_settings.py，替换IP:PORT添加：

```
# Enable Only Office
ENABLE_ONLYOFFICE = True
VERIFY_ONLYOFFICE_CERTIFICATE = False
# ONLYOFFICE_APIJS_URL = 'http{s}://{your OnlyOffice server's domain or IP}/web-apps/apps/api/documents/api.js'
ONLYOFFICE_APIJS_URL = 'http://IP:PORT/web-apps/apps/api/documents/api.js'
ONLYOFFICE_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
ONLYOFFICE_EDIT_FILE_EXTENSION = ('docx', 'pptx', 'xlsx')
```