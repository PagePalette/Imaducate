import json

fd = open('.env/conf.json')
cf = json.load(fd)

RELEASE_MODE = 0
TEST_MODE = 1

API_KEY = cf['api-key']
MODE = {
    "release": RELEASE_MODE,
    "testing": TEST_MODE
}[cf['deploy-mode']]

print("MODE: ", MODE)
