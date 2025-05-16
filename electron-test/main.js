const { app, BrowserWindow } = require('electron');
const path  = require('path');

const isMac = process.platform === 'darwin';

const isDev = process.env.NODE_ENV !== 'production'

function createMainWindow() {
    const mainWindow = new BrowserWindow({
        title: 'PER Grader',
        width: isDev ? 1000 : 500,
        height: 800,
    })

    // open dev tools if in dev
    // if (isDev) {
    //     mainWindow.webContents.openDevTools();
    // }

    mainWindow.loadFile(path.join(__dirname, './renderer/index.html'))
}

app.whenReady().then(() => {
    createMainWindow();

    // Open a window if none are open (macOS)
    app.on('activate', () => {
      if (BrowserWindow.getAllWindows().length === 0) createMainWindow();
    });
})

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  if (!isMac) app.quit();
});
