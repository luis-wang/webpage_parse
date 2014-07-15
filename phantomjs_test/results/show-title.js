var page = require('webpage').create();
var url = 'http://www.csdn.net/article/2014-07-15/2820656';
page.open(url, function(status) {
  var title = page.evaluate(function() {
    return document.title;
  });
  console.log('Page title is ' + title);
});