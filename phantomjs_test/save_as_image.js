var page = require('webpage').create();
page.open('http://www.csdn.net/', function() {
  page.render('csdn.png');
  phantom.exit();
});