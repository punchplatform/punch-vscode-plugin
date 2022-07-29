'use strict';

import * as vscode from 'vscode'

let terminal : vscode.Terminal = vscode.window.createTerminal("Puncher")
let docker = 'docker run -v'

export function runPuncher(filePath : any){
    //var p = cp.exec("docker run -v /home/guillaume/Documents/codeAssit/punch-sample-parser:/workdir/ ghcr.io/punchplatform/puncher:8.0-dev -p /workdir/puncher.punch", (err, stdout, stderr) => {
    //    console.log(stdout)
    //});
    if(filePath != undefined){
        filePath = filePath.toString()
        let folderPath = filePath.substring(0,filePath.lastIndexOf('/'))
        let filename = filePath.substring(filePath.lastIndexOf('/')+1)
        let command = docker + ' ' + folderPath + ':/workdir/ ghcr.io/punchplatform/puncher:8.0-dev -p /workdir/' + filename
        terminal.show()
        terminal.sendText(command)
    } else {
        vscode.window.showErrorMessage("No punch file open")
    }
    
    
}