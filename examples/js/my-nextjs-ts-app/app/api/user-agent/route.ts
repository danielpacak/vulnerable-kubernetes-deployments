import { headers } from 'next/headers'

export async function GET() {
    const headersList = await headers()
    const userAgent = headersList.get('user-agent')

    return Response.json({ userAgent })
}
