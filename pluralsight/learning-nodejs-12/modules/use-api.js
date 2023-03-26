const api = require('./use-api/api');
console.log(api.language, api.direction, api.encoding);

console.log(require('./use-api/array'));

// printing template
const template_api = require('./use-api/template');
console.log(template_api('Harsh'));