import * as child_process from "node:child_process";
import * as util from "node:util"


// Convert exec to a promise-based function
const execPromise = util.promisify(child_process.exec);

async function executeCommand(command: string): Promise<string> {
    try {
        const {stdout, stderr} = await execPromise(command);

        if (stderr) {
            console.error(`Command stderr: ${stderr}`);
        }

        console.log(`Command output:\n${stdout}`);
        return stdout;
    } catch (e) {
        let message: string
        if (typeof e === "string") {
            message = e.toUpperCase() // works, `e` narrowed to string
        } else if (e instanceof Error) {
            message = e.message // works, `e` narrowed to Error
        } else {
            message = "unknown error"
        }

        console.error(`Error executing command: ${message}`);
        throw e;
    }
}

export async function GET() {
    let out: string = await executeCommand("uname -r")
    return Response.json({"foo": "bar", "out": out})
}
