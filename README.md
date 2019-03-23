# What's New (on GDrive)

A small app to resolve a Google Drive folder to its newest file.

## Usage

If this app is hosted at `http://example.com`, you would append the
URL to a readable Google Drive folder like so:

[`http://example.com?folder_url=https://drive.google.com/drive/u/0/folders/1zGubetz_yE-Lt4jI98MtqnwY8FBZZGnt`][example1]

[example1]: http://example.com?folder_url=https://drive.google.com/drive/u/0/folders/1zGubetz_yE-Lt4jI98MtqnwY8FBZZGnt

### Additional Options

By default, the app will redirect to the most recently _created_ file
listed in the folder. You may also select based on other fields, like
so:

[`http://example.com?folder_url=https://drive.google.com/drive/u/0/folders/1zGubetz_yE-Lt4jI98MtqnwY8FBZZGnt&select_by=modifiedDate`][example2]

[example2]: http://example.com?folder_url=https://drive.google.com/drive/u/0/folders/1zGubetz_yE-Lt4jI98MtqnwY8FBZZGnt&select_by=modifiedDate

<!-- Everything above this linebreak will appear on app homepage. -->
---
<!-- Everything below will only be in the repository README. -->

## :computer: Local Development

These instructions assume that [`pipenv`][1] is installed.

[1]: http://example.com

```
cp sample.env .env
pipenv install

pipenv run gunicorn app:app --log-file -
```

## Configuration

A Google service account keyfile is needed in order for this app to
work. You may generate a keyfile via [these instructions][keyfile].

[keyfile]: https://cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-console

You may then either store the file as `service-key.json` in the project
root directory, or you may convert the keyfile into a base64-encoded
string, and store that in `GOOGLE_CREDS_BASE64`. For example, on
linux-based systems:

    export GOOGLE_CREDS_BASE64="$( cat service-key.json | base64 )"

## Deployment

- The [demo heroku app][demo] will auto-deploy all changes to `master` branch
  on GitHub.
- To self-host you own version, use the "Deploy to Heroki" button.
  [`#TODO`](https://www.heroku.com/elements/buttons)

   [demo]: https://gdrive-whats-new-app.herokuapp.com/

## :copyright: License

GPL3
