# ckanext-mermaid

CKAN Extension for user context testing. Easily mask your user role, organization, and permissions in the front-end to perform faster end-to-edn testing.


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | Not tested    |
| 2.7             | Not tested    |
| 2.8             | Not tested    |
| 2.9             | Not tested    |
| 2.10            | Not tested    |
| 2.11            | Not tested    |
| 2.12            | Yes    |

| Python version    | Compatible?   |
| --------------- | ------------- |
| 2.9 and earlier | Not tested    |
| 3.0 and later             | Yes    |

## Installation

To install ckanext-test-context:

1. Activate your CKAN virtual environment, for example:

     `. /usr/lib/ckan/default/bin/activate`

2. Clone the source and install it on the virtualenv

    - `git clone --branch main --single-branch https://github.com/JVickery-TBS/ckanext-test-context.git`
    - `cd ckanext-test-context`
    - `pip install -e .`
    - `pip install -r requirements.txt`

3. Add `test_context` to the `ckan.plugins` setting in your CKAN
   config file

4. Restart CKAN
