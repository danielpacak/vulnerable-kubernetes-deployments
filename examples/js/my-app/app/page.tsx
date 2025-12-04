import Link from 'next/link'
import Greeting from './components/Greeting'
import Counter from './components/Counter'

export default function Page() {
    return (
        <div>
            <h1>Hello, Hext.js!</h1>
            {/* Prefetched when the link is hovered or enters the viewport */}
            <Link href="/blog">Blog</Link>
            {/* Renders Server and Client Components */}
            <Greeting name="John" />
            <Greeting name="Daniel" />
            <Counter />
        </div>
    );
}
