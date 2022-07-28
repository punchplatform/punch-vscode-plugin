'use strict';
import * as cp from "child_process";

export function runPuncher(){
    var p = cp.exec("docker run -v /home/guillaume/Documents/codeAssit/punch-sample-parser:/workdir/ ghcr.io/punchplatform/puncher:8.0-dev -p /workdir/puncher.punch", (err, stdout, stderr) => {
        console.log(stdout)
    });
    
}