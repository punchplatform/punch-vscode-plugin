// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import {PunchDocumentRangeFormatter, MODE} from './formatter';
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	const formatter = new PunchDocumentRangeFormatter();
	context.subscriptions.push(vscode.commands.registerCommand('punch.Punchlet', () => {
				
		})
	);

	context.subscriptions.push(vscode.languages.registerDocumentFormattingEditProvider(MODE, formatter));
}

// this method is called when your extension is deactivated
export function deactivate() {

}
