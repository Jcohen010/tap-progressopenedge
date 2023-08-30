# tap-progressopenedge

`tap-progressopenedge` is a Singer tap for ProgressOpenEdge.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

<!--

Developer TODO: Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

## Installation

Install from PyPi:

```bash
pipx install tap-progressopenedge
```

Install from GitHub:

```bash
pipx install git+https://github.com/ORG_NAME/tap-progressopenedge.git@main
```

-->
## Prerequisites
### OpenEdge ODBC Driver
In order for this tap to successfully connect to the progress openedge database, the user must have a Data Direct OpenEdge ODBC driver installed and configured on their device. It would be wise to test the connection to the source through the ODBC driver before using the tap.

#### Installation
View the installation guide [here](https://docs.progress.com/bundle/datadirect-odbc-installation/page/Copyright.html).

View the getting started (configuration and adding a new connection) guide [here](https://docs.progress.com/bundle/datadirect-connect-odbc-71/page/Quick-Start-Connect.html).

View the user guide [here](https://docs.progress.com/bundle/datadirect-connect-odbc-71/page/The-Progress-OpenEdge-Wire-Protocol-Driver.html).





## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-progressopenedge --about --format=markdown
```
-->

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-progressopenedge --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

## Usage

You can easily run `tap-progressopenedge` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-progressopenedge --version
tap-progressopenedge --help
tap-progressopenedge --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-progressopenedge` CLI interface directly using `poetry run`:

```bash
poetry run tap-progressopenedge --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-progressopenedge
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-progressopenedge --version
# OR run a test `elt` pipeline:
meltano elt tap-progressopenedge target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
