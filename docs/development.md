## Contributing

This project is an open source implementation of a scientific research paper. Because this is an academic project, we would appreciate it if you would let us know how you intend to use the software (other than simply copying and pasting code so that you can use it in your own projects). If you would like to contribute, you can do so in the following ways:

- Add issues or bugs to the bug tracker: [https://github.com/DistrictDataLabs/semnet-similarity/issues](https://github.com/DistrictDataLabs/semnet-similarity/issues)
- Work on a card on the dev board: [https://waffle.io/DistrictDataLabs/semnet-similarity](https://waffle.io/DistrictDataLabs/semnet-similarity)
- Create a pull request in Github: [https://github.com/DistrictDataLabs/semnet-similarity/pulls](https://github.com/DistrictDataLabs/semnet-similarity/pulls)

If you are a member of the DDL Research Labs Semantic Network Extraction group, you have direct access to the repository, which is set up in a typical production/release/development cycle as described in [A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/). A typical workflow is as follows:

1. Select a card from the [dev board](https://waffle.io/DistrictDataLabs/semnet-similarity) - preferably one that is "ready" then move it to "in-progress".

2. Create a branch off of develop called "feature-[feature name]", work and commit into that branch.

        ~$ git checkout -b feature-myfeature develop

3. Once you are done working (and everything is tested) merge your feature into develop.

        ~$ git checkout develop
        ~$ git merge --no-ff feature-myfeature
        ~$ git branch -d feature-myfeature
        ~$ git push origin develop

4. Repeat. Releases will be routinely pushed into master via release branches, then deployed to the server.
