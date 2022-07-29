'use strict';

import * as vscode from 'vscode'

let terminal: vscode.Terminal = vscode.window.createTerminal("Puncher");
let docker = 'docker run -v';

export function runPuncher(filePath: any) {

    if (filePath != undefined) {
        let tag = vscode.workspace.getConfiguration('punch-puncher')['puncherTag'];
        filePath = filePath.toString();
        let folderPath = filePath.substring(0, filePath.lastIndexOf('/'));
        let filename = filePath.substring(filePath.lastIndexOf('/') + 1);
        let command = docker + ' ' + folderPath + ':/workdir/ ghcr.io/punchplatform/puncher:' + tag +  ' -p /workdir/' + filename;
        terminal.show();
        terminal.sendText(command);
    } else {
        vscode.window.showErrorMessage("No punch file open");
    }

}