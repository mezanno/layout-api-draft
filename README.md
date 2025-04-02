# layout-api-draft
Preliminary work on layout API: API gateway, naive Gallica cache and layout worker.

## Build
Clone worker's sources:
```sh
git clone --depth 1 https://github.com/soduco/directory-annotator-back.git worker/code
```

Then build and run everything at once:
```sh
docker compose up
```

## Use

Sample URL
`http://127.0.0.1:8200/layout?image_url=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/bd6t543045578/f10/full/max/0/default.webp`


## Clean-up
```sh
docker compose down; docker image rm layout-api-draft-api-gateway layout-api-draft-cache:latest layout-api-draft-worker-wrapper:latest layout-api-draft-worker:latest
```
