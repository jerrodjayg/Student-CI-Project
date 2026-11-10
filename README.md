# Student-CI-Project

A small Python calculator project for the CMSC 426 Jenkins + GitHub Continuous Integration assignment.

## Requirements
- Python 3 (available as `python` on your machine and Jenkins agent)
- Git
- Jenkins with the Git plugin (for Jenkins runs)

No third-party Python packages are required.

## Run locally
```bat
python app.py
python -m unittest discover -s tests -v
```

On Windows, you can also run:
```bat
build.bat
```

## Configure Jenkins (Windows Freestyle job)
1. Create a **Freestyle project** named `Student-CI-Project`.
2. Under **Source Code Management**, select **Git** and enter your GitHub repository's HTTPS clone URL.
3. For a public repo, leave **Credentials** as `- none -`. For a private repo, use a Jenkins-stored credential; never paste a token in the repository URL or build command.
4. Choose your branch (usually `*/main`).
5. Under **Build Steps**, add **Execute Windows batch command** with `call build.bat`.
6. Save and click **Build Now**. Check **Console Output** for four passing tests and `SUCCESS`.

## Configure an automatic trigger
If a publicly reachable webhook endpoint is available, enable **GitHub hook trigger for GITScm polling** in Jenkins. In your GitHub repository, go to **Settings > Webhooks > Add webhook**. Set payload URL to `https://YOUR-HTTPS-ENDPOINT/github-webhook/` with content type `application/json` and push events enabled. Verify a webhook delivery and corresponding Jenkins build.

If no public endpoint is available, select **Poll SCM** in Jenkins and use the schedule `H/5 * * * *`. Push a change, wait for Jenkins polling, and verify the automatically started build. Your assignment allows this alternative if the webhook cannot be configured due to restrictions; document the limitation and collect evidence. Polling is an alternative, not proof that a webhook worked.

## Demonstrate a failed build and recovery
1. First confirm tests pass and screenshot Jenkins `SUCCESS` + console output.
2. Temporarily change the expected value in `test_add_positive_numbers` from `5` to `6`.
3. Commit and push; allow the trigger to run or build manually, and screenshot `FAILURE` + console output.
4. Restore the expectation to `5`, commit and push again, and verify the final build returns to `SUCCESS`.
5. **Do not submit with the test intentionally broken.**

## Security
- Enable Jenkins authentication and least-privilege permissions.
- Use HTTPS when exposing webhook endpoints and validate webhook secrets where supported.
- Store credentials in Jenkins Credentials, not in code or screenshots.
- Never disable Jenkins security or CSRF protection as a troubleshooting shortcut.
