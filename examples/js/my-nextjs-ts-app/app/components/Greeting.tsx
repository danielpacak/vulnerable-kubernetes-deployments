import {ReactNode} from "react";

type GreetingProps = {
    name: string
}

{/* Server Component */}
export default function Greeting(props: GreetingProps): ReactNode {
    console.log(`Rendering Greeting component on the server ${props.name}...`)
    return <p>Hello, {props.name}! Rendered on the server.</p>
}
