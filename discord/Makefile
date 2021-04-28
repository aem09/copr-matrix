
version = v1.0.0

# This requires https://www.npmjs.com/package/npm-pack-all

.ONESHELL:
pack:
	git clone https://github.com/Half-Shot/matrix-appservice-discord.git
	cd matrix-appservice-discord
	git checkout ${version}
	npm install
	npm-pack-all --output ..
	cd ..
	rm -rf matrix-appservice-discord
