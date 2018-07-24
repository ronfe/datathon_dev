/**
 * Created by jihongfei on 7/17/18.
 */

const {app, BrowserWindow} = require('electron');

let win = null;

function quit() {
  win = null;
}

app.on('ready', function(){
  win = new BrowserWindow({width: 1000, height:600});
  win.loadURL('http://localhost:8080');
  win.on('closed', quit);
});

app.on('activate', function(){
  if (win === null) {
  createWindow();
}
});

app.on('window-all-closed', function () {
  if (process.platform != 'darwin') {
    app.quit();
  }
});
