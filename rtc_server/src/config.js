const yaml = require('js-yaml')
const fs = require('fs')
const path = require('path')

module.exports = (configName) => {
    try {
        return yaml.safeLoad(fs.readFileSync(path.resolve(__dirname, `../../configs/${configName}.yaml`)))
    } catch(e) {
        console.log(`Error occured loading configuration: ${e}`)
        throw e
    }
}