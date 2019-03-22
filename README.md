# What's New (on GDrive)

A small app to resolve a Google Drive folder to its newest file.

**Note:** This is a work-in-progress, and not yet functional.

## Usage

If this app is hosted at `http://example.com`, you would append the
URL to a readable Google Drive folder like so:

[`http://example.com?folder_url=https://drive.google.com/drive/u/0/folders/1zGubetz_yE-Lt4jI98MtqnwY8FBZZGnt`][sample]

[sample]: http://example.com?folder_url=https://drive.google.com/drive/u/0/folders/1zGubetz_yE-Lt4jI98MtqnwY8FBZZGnt

The app will redirect to the most recently created file listed in the
folder!

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

## Deployment

- The [demo heroku app][demo] will auto-deploy all changes to `master` branch
  on GitHub.
- To self-host you own version, use the "Deploy to Heroki" button.
  [`#TODO`](https://www.heroku.com/elements/buttons)

   [demo]: https://gdrive-whats-new-app.herokuapp.com/

## :copyright: License

GPL3
