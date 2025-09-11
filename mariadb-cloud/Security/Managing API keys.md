# Managing API keys

## **Getting Started with API Keys**
1. Go to SkySQL API Key management page: https://app.skysql.com/user-profile/api-keys and generate an API key

2. Export the value from the token field to an environment variable $API_KEY

3. Use it on subsequent request, e.g:
```bash 
 curl --request GET 'https://api.skysql.com/provisioning/v1/services' \
 --header "X-API-Key: $API_KEY"
```

## **Managing API Keys**

Use the [Portal](https://app.skysql.com/user-profile/api-keys) to create new, revoke or permanently delete these Keys.  

OR

You can use the swagger API portal to manage the keys.

1. [Fetch all keys](https://apidocs.skysql.com/#/allowed_roles:ADMIN;MEMBER/get_organization_v1_users__user_id__api_keys)

2. [Create a new API Key](https://apidocs.skysql.com/#/allowed_roles:ADMIN;MEMBER/post_organization_v1_users__user_id__api_keys)

3. [Delete a user specific Key](https://apidocs.skysql.com/#/allowed_roles:ADMIN;MEMBER/get_organization_v1_users__user_id__api_keys__key_id_)

4. [Update a user specific key ](https://apidocs.skysql.com/#/allowed_roles:ADMIN;MEMBER/patch_organization_v1_users__user_id__api_keys__key_id_)
